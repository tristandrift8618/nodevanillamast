"""detector_eb13bc - Resource manager."""
from contextlib import contextmanager
import time, json
RESOURCE_ID = "detector_eb13bc"
@contextmanager
def managed_resource(name: str):
    start = time.time()
    print(f"[{RESOURCE_ID}] Acquiring: {name}")
    try: yield {"name": name, "owner": RESOURCE_ID}
    finally: print(f"[{RESOURCE_ID}] Released: {name} ({time.time()-start:.3f}s)")
def process_with_resources(resources: list) -> list:
    results = []
    for r in resources:
        with managed_resource(r) as ctx:
            results.append({**ctx, "status": "processed"})
    return results
def main():
    resources = ["db-conn", "file-lock", "cache-slot"]
    results = process_with_resources(resources)
    print(f"[{RESOURCE_ID}] Results: {json.dumps(results, indent=2)}")
if __name__ == "__main__":
    main()
