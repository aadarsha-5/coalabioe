def page_restoring(pages, capacity):
    cache = []
    hits = 0
    page_faults = 0
    total_requests = len(pages)
    frame_sequence = []

    for page in pages:
        if page in cache:
            hits += 1
        else:
            if len(cache) < capacity:
                cache.append(page)
            else:
                cache.pop(0)
                cache.append(page)
                page_faults += 1

        frame_sequence.append(cache[:])

    hit_ratio = hits / total_requests
    return hit_ratio, page_faults, frame_sequence

# Prompt the user for the number of pages
num_pages = int(input("Enter the number of pages: "))

# Prompt the user for the number of cache slots
num_cache = int(input("Enter the number of cache slots: "))

# Prompt the user for the page reference string
page_references = input("Enter the page reference string (space-separated): ").split()
page_references = [int(page) for page in page_references]

# Calculate the hit ratio, page faults, and frame sequence
hit_ratio, faults, frames = page_restoring(page_references, num_cache)

# Print the hit ratio
print("Hit ratio:", hit_ratio)

# Print the page fault count
print("Page Faults:", faults)

# Print the frame sequence
print("Frame Sequence:")
for i, frame in enumerate(frames):
    print("Step", i+1, ":", frame)
