import timeit
import matplotlib.pyplot as plt
from subset import subset_sum_dc, subset_sum_dp

def random_list(n, max_value=100):
    import random
    return [random.randint(1, max_value) for _ in range(n)]
def measure_time(func, arr, target):
    start_time = timeit.default_timer()
    func(arr, target)
    end_time = timeit.default_timer()
    return end_time - start_time
def test_performance(max_n, num_tests=10):
    dc_times = []
    dp_times = []
    for n in range(1, max_n+1):
        dc_time = 0
        dp_time = 0
        for _ in range(num_tests): # Varios intentos de input para un mismo tamaño de input
            arr = random_list(n) # Se genera un array que se utiliza en ambos algoritmos
            target = int(sum(arr)/2)

            dc_time += measure_time(subset_sum_dc, arr, target)
            dp_time += measure_time(subset_sum_dp, arr, target)

        dc_times.append(dc_time / num_tests) # Rendimiento promedio por tamaño
        dp_times.append(dp_time / num_tests)
    return dc_times, dp_times

def plot_performance(max_n, dc_times, dp_times):
    plt.plot(range(1, max_n+1), dc_times, label='Divide and Conquer')
    plt.plot(range(1, max_n+1), dp_times, label='Programación dinamica')
    plt.xlabel('Tamaño de subset (n)')
    plt.ylabel('Tiempo promedio (s)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # a) Son 100 tamaños de entrada
    max_n = 1000
    step = 1
    dc_times, dp_times = test_performance(max_n, step)
    # b) Grafica 
    plot_performance(max_n, dc_times, dp_times)
    