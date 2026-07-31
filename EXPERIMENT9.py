import math

def first_fit(items, capacity=1.0):
    """Places each item into the first bin with enough space."""
    remaining_space = []
    bin_contents = []

    for item in items:
        placed = False

        for i, space in enumerate(remaining_space):
            if space >= item:
                remaining_space[i] -= item
                bin_contents[i].append(item)
                placed = True
                break

        if not placed:
            remaining_space.append(capacity - item)
            bin_contents.append([item])

    return bin_contents

def first_fit_decreasing(items, capacity=1.0):
    """Sort items in decreasing order, then apply First Fit."""
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)

def best_fit_decreasing(items, capacity=1.0):
    """Sort items in decreasing order and place each item in the best-fitting bin."""
    sorted_items = sorted(items, reverse=True)

    remaining_space = []
    bin_contents = []

    for item in sorted_items:
        best_index = -1
        minimum_leftover = float("inf")

        for i, space in enumerate(remaining_space):
            if space >= item and (space - item) < minimum_leftover:
                minimum_leftover = space - item
                best_index = i

        if best_index != -1:
            remaining_space[best_index] -= item
            bin_contents[best_index].append(item)
        else:
            remaining_space.append(capacity - item)
            bin_contents.append([item])

    return bin_contents

def display_bins(title, bins, capacity=1.0):
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)

    for i, current_bin in enumerate(bins, start=1):
        used = sum(current_bin)
        remaining = capacity - used
        utilization = (used / capacity) * 100

        bar = "#" * int(utilization / 5)

        print(
            f"Bin {i:2d}: {current_bin}"
            f"\n        Used      : {used:.1f}"
            f"\n        Remaining : {remaining:.1f}"
            f"\n        Utilization: {utilization:.0f}% [{bar:<20}]"
        )

    print(f"\nTotal Bins Used: {len(bins)}")

def main():

    items = [0.5, 0.7, 0.3, 0.9, 0.2,
             0.6, 0.8, 0.4, 0.1, 0.5]

    capacity = 1.0

    total_size = sum(items)
    lower_bound = math.ceil(total_size / capacity)

    print("=" * 60)
    print("BIN PACKING APPROXIMATION ALGORITHMS")
    print("=" * 60)

    print(f"Items               : {items}")
    print(f"Bin Capacity        : {capacity}")
    print(f"Total Item Size     : {total_size:.1f}")
    print(f"Theoretical Lower Bound (Optimal) : {lower_bound}")
    ff_bins = first_fit(items, capacity)
    ffd_bins = first_fit_decreasing(items, capacity)
    bfd_bins = best_fit_decreasing(items, capacity)
    display_bins("First Fit (FF)", ff_bins, capacity)
    display_bins("First Fit Decreasing (FFD)", ffd_bins, capacity)
    display_bins("Best Fit Decreasing (BFD)", bfd_bins, capacity)
    print("\n" + "=" * 60)
    print("ALGORITHM COMPARISON")
    print("=" * 60)
    print(f"{'Algorithm':<25}{'Bins Used'}")
    print("-" * 40)
    print(f"{'Lower Bound (Optimal)':<25}{lower_bound}")
    print(f"{'First Fit (FF)':<25}{len(ff_bins)}")
    print(f"{'First Fit Decreasing':<25}{len(ffd_bins)}")
    print(f"{'Best Fit Decreasing':<25}{len(bfd_bins)}")
    print("\nEfficiency (Lower is Better)")
    print(f"FF  : {len(ff_bins) - lower_bound} extra bin(s)")
    print(f"FFD : {len(ffd_bins) - lower_bound} extra bin(s)")
    print(f"BFD : {len(bfd_bins) - lower_bound} extra bin(s)")

if __name__ == "__main__":
    main()