import time
import random
import matplotlib.pyplot as plt
from ternary_search_tree import TernarySearchTree


def load_word_list(filepath, limit=None):
    with open(filepath, 'r') as file:
        words = [line.strip() for line in file if line.strip()]
    return words[:limit] if limit else words


def benchmark_tst(word_list, sizes):
    results = []

    for size in sizes:
        sample_words = word_list[:size]
        tst = TernarySearchTree()

        # Measure insertion time
        insert_start = time.perf_counter()
        for word in sample_words:
            tst.insert(word)
        insert_end = time.perf_counter()

        # Measure search time
        test_words = random.sample(sample_words, min(1000, len(sample_words)))
        search_start = time.perf_counter()
        for word in test_words:
            tst.search(word, exact=True)
        search_end = time.perf_counter()

        results.append({
            "size": size,
            "insert_time": round(insert_end - insert_start, 4),
            "search_time": round(search_end - search_start, 4)
        })

    return results


def display_results(results):
    print(f"{'Words':>8} | {'Insert (s)':>12} | {'Search (s)':>12}")
    print("-" * 37)
    for r in results:
        print(f"{r['size']:>8} | {r['insert_time']:>12.4f} | {r['search_time']:>12.4f}")


def plot_results(results):
    sizes = [r['size'] for r in results]
    insert_times = [r['insert_time'] for r in results]
    search_times = [r['search_time'] for r in results]
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, insert_times, marker='o', label='Insert Time')
    plt.plot(sizes, search_times, marker='s', label='Search Time')
    plt.xlabel('Number of Words')
    plt.ylabel('Time (seconds)')
    plt.title('Ternary Search Tree Performance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("benchmark_plot.png")
    print("Plot saved as 'benchmark_plot.png'")
    plt.show()


if __name__ == "__main__":
    print("Starting Benchmark Script...")
    filepath = "data/search_trees/corncob_lowercase.txt"
    input_sizes = [100, 750, 1500, 3000, 6000, 12000]
    word_list = load_word_list(filepath)
    benchmark_data = benchmark_tst(word_list, input_sizes)
    display_results(benchmark_data)
    plot_results(benchmark_data)
