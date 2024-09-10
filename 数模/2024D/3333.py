import numpy as np
from scipy.stats import norm

# 假设你的命中概率函数是以下形式
def calculate_hit_probability(h):
    # 示例实现：假设命中概率是一个正态分布的累积分布函数
    mean_depth = 150  # 假设潜艇中心位置的深度定位值为150米
    std_depth = 40    # 假设标准差为40米
    hit_probability = norm.cdf(h, loc=mean_depth, scale=std_depth)
    return hit_probability

# 灰狼优化算法
class GreyWolfOptimizer:
    def __init__(self, objective_func, n_wolves, bounds, max_iter):
        self.objective_func = objective_func
        self.n_wolves = n_wolves
        self.bounds = bounds
        self.max_iter = max_iter
        self.dim = len(bounds)
        self.alpha_pos = None
        self.beta_pos = None
        self.delta_pos = None
        self.init_population()
    
    def init_population(self):
        self.wolves = np.array([np.random.uniform(low, high, self.dim) for low, high in self.bounds])
    
    def update_position(self, a):
        for i in range(self.n_wolves):
            # Update alpha, beta, and delta
            if self.alpha_pos is not None:
                A1 = 2 * a * np.random.rand() - a
                C1 = 2 * np.random.rand()
                D_alpha = abs(self.alpha_pos - self.wolves[i])
                X1 = self.alpha_pos - A1 * D_alpha
            else:
                X1 = self.wolves[i]
            
            if self.beta_pos is not None:
                A2 = 2 * a * np.random.rand() - a
                C2 = 2 * np.random.rand()
                D_beta = abs(self.beta_pos - self.wolves[i])
                X2 = self.beta_pos - A2 * D_beta
            else:
                X2 = self.wolves[i]
            
            if self.delta_pos is not None:
                A3 = 2 * a * np.random.rand() - a
                C3 = 2 * np.random.rand()
                D_delta = abs(self.delta_pos - self.wolves[i])
                X3 = self.delta_pos - A3 * D_delta
            else:
                X3 = self.wolves[i]
            
            self.wolves[i] = (X1 + X2 + X3) / 3  # Update the position of the current wolf
    
    def optimize(self):
        for t in range(self.max_iter):
            # Evaluate fitness of each wolf
            fitness = np.array([self.objective_func(wolf) for wolf in self.wolves])
            
            # Update alpha, beta, and delta wolves
            sorted_indices = np.argsort(fitness)
            self.alpha_pos = self.wolves[sorted_indices[0]]
            if len(sorted_indices) > 1:
                self.beta_pos = self.wolves[sorted_indices[1]]
            if len(sorted_indices) > 2:
                self.delta_pos = self.wolves[sorted_indices[2]]
            
            # Update the position of the wolves
            a = 2 - 2 * (t / self.max_iter)  # a decreases linearly from 2 to 0
            self.update_position(a)
        
        # Return the best solution
        best_fitness = np.max(fitness)
        best_wolf = self.wolves[np.argmax(fitness)]
        return best_wolf, best_fitness

# Define the problem bounds (e.g., depth range)
min_depth = 120  # 潜艇中心位置实际深度的最小值
max_depth = 200  # 假设的最大深度
bounds = [(min_depth, max_depth)]

# Initialize the optimizer
gwo = GreyWolfOptimizer(calculate_hit_probability, n_wolves=10, bounds=bounds, max_iter=100)

# Run the optimization
best_depth, best_hit_probability = gwo.optimize()

print(f"Best depth: {best_depth}")
print(f"Best hit probability: {best_hit_probability}")