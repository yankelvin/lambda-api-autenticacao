from datetime import datetime


def serialize_document(document: dict) -> dict:
    """Converte ObjectId e datetime em strings para que o documento seja serializável em JSON."""
    if not document:
        return document

    for key, value in document.items():
        if isinstance(value, datetime):
            document[key] = value.isoformat()
        elif isinstance(value, dict):
            document[key] = serialize_document(value)

    return document
