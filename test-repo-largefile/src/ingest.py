import csv
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterator
import logging

log = logging.getLogger(__name__)

def stream_csv(path: Path, chunk_size: int = 1000) -> Iterator[list[dict]]:
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

def parse_catalog(path: Path) -> Iterator[dict]:
    context = ET.iterparse(path, events=('end',))
    for event, elem in context:
        if elem.tag == 'item':
            yield {'id': elem.get('id'),
                   'sku': elem.findtext('sku'),
                   'name': elem.findtext('name'),
                   'category': elem.findtext('category'),
                   'price': elem.findtext('price')}
            elem.clear()

def count_lines(path: Path) -> int:
    with open(path, 'rb') as f:
        return sum(1 for _ in f)

def summarize(data_dir: Path) -> dict:
    summary = {}
    for p in data_dir.iterdir():
        if p.is_file():
            summary[p.name] = {'size_bytes': p.stat().st_size,
                                'lines': count_lines(p)}
    return summary
