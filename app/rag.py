"""Secure, local document retrieval for the BonganiSecure AI portfolio."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "sample_documents.json"
)


class DocumentStore:
    """Load synthetic documents and retrieve only authorised matches."""

    def __init__(self, data_path: str | Path = DEFAULT_DATA_PATH) -> None:
        self._data_path = Path(data_path)
        self._documents = self._load_documents()

    def _load_documents(self) -> list[dict[str, Any]]:
        with self._data_path.open("r", encoding="utf-8") as file:
            documents = json.load(file)

        if not isinstance(documents, list):
            raise ValueError("The document dataset must be a JSON list.")

        seen_ids: set[str] = set()

        for document in documents:
            if not isinstance(document, dict):
                raise ValueError("Each document must be a JSON object.")

            document_id = document.get("id")
            title = document.get("title")
            content = document.get("content")
            groups = document.get("allowed_groups")

            if not isinstance(document_id, str) or not document_id.strip():
                raise ValueError("Every document must have a non-empty ID.")

            if document_id in seen_ids:
                raise ValueError(f"Duplicate document ID: {document_id}")

            seen_ids.add(document_id)

            if not isinstance(title, str) or not isinstance(content, str):
                raise ValueError("Document title and content must be strings.")

            if (
                not isinstance(groups, list)
                or not groups
                or not all(
                    isinstance(group, str) and group.strip()
                    for group in groups
                )
            ):
                raise ValueError(
                    f"Document {document_id} must have valid allowed_groups."
                )

        return documents

    def search(
        self,
        query: str,
        trusted_user_groups: set[str] | frozenset[str],
        limit: int = 5,
    ) -> list[dict[str, str]]:
        """
        Search documents accessible to trusted_user_groups.

        The caller must obtain these groups from a trusted identity source.
        Never populate them directly from an untrusted request parameter.
        """
        if not isinstance(query, str) or not query.strip():
            raise ValueError("Query must not be empty.")

        if not isinstance(trusted_user_groups, (set, frozenset)):
            raise TypeError("User groups must be provided as a set.")

        if not all(
            isinstance(group, str) and group.strip()
            for group in trusted_user_groups
        ):
            raise ValueError("User groups must contain non-empty strings.")

        if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
            raise ValueError("Limit must be a positive integer.")

        terms = set(query.casefold().split())
        matches: list[dict[str, str]] = []

        # Authorisation filtering occurs before content matching.
        authorised_documents = [
            document
            for document in self._documents
            if trusted_user_groups.intersection(document["allowed_groups"])
        ]

        for document in authorised_documents:
            searchable_text = (
                document["title"] + " " + document["content"]
            ).casefold()

            if any(term in searchable_text for term in terms):
                matches.append(
                    {
                        "id": document["id"],
                        "title": document["title"],
                        "content": document["content"],
                    }
                )

            if len(matches) >= limit:
                break

        return matches


def retrieve_documents(
    query: str,
    trusted_user_groups: set[str] | frozenset[str],
    data_path: str | Path = DEFAULT_DATA_PATH,
    limit: int = 5,
) -> list[dict[str, str]]:
    """Convenience function for retrieving authorised documents."""
    store = DocumentStore(data_path)
    return store.search(query, trusted_user_groups, limit)
