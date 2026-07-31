import random
import time
import sys
sys.setrecursionlimit(20000)
comparisons = 0
def partition(arr, low, high):
    global comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)
def randomized_quicksort(arr, low, high):
    if low < high:
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]

        pivot_index = partition(arr, low, high)

        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)
def run_test(sort_function, arr):
    global comparisons

    copied_array = arr[:]
    comparisons = 0

    start_time = time.perf_counter()

    sort_function(copied_array, 0, len(copied_array) - 1)

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    return comparisons, execution_time
def main():

    N = 5000
    test_cases = {
        "Random": [random.randint(1, 100000) for _ in range(N)],
        "Sorted": list(range(N)),
        "Reverse Sorted": list(range(N, 0, -1)),
        "Nearly Sorted": list(range(N))
    }
    nearly_sorted = test_cases["Nearly Sorted"]

    for _ in range(N // 20):
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]

    print("=" * 90)
    print("QUICK SORT PERFORMANCE COMPARISON")
    print("=" * 90)

    print(f"Array Size : {N}")

    print("-" * 90)
    print(
        f"{'Input Type':<18}"
        f"{'DQS Comparisons':>18}"
        f"{'DQS Time(ms)':>16}"
        f"{'RQS Comparisons':>18}"
        f"{'RQS Time(ms)':>16}"
    )
    print("-" * 90)

    for case, array in test_cases.items():

        dqs_comp, dqs_time = run_test(deterministic_quicksort, array)

        rqs_comp, rqs_time = run_test(randomized_quicksort, array)

        print(
            f"{case:<18}"
            f"{dqs_comp:>18}"
            f"{dqs_time:>16.2f}"
            f"{rqs_comp:>18}"
            f"{rqs_time:>16.2f}"
        )

    print("-" * 90)

    print("\nObservation:")
    print("• Deterministic Quick Sort performs efficiently on random data.")
    print("• On already sorted and reverse sorted arrays,")
    print("  Deterministic Quick Sort performs poorly because")
    print("  the pivot selection becomes unbalanced (worst case O(n²)).")
    print("• Randomized Quick Sort selects pivots randomly,")
    print("  reducing the chance of worst-case behavior.")
    print("• Therefore, Randomized Quick Sort generally achieves")
    print("  an average-case complexity close to O(n log n).")
if __name__ == "__main__":
    main()