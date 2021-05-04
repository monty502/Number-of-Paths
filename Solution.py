def num_of_paths_to_dest(n):
  # there's only 1 path to reach every cell in row 0
  dp = [1] * n
  
  # from row 1 on, dp[col] represents number of paths to square[row, col]
  for row in range(1, n):
    for col in range(row, n):
      # if the square is on diagnal line, the only paths are from below
      # otherwise, the paths are either from below, or from left:
      #             5
      #             ^
      #         2 > 5
      #         ^   ^
      #     1 > 2 > 3
      #     ^   ^   ^
      # 1 > 1 > 1 > 1
      if col > row:
        dp[col] += dp[col - 1]
  
  return dp[n-1]

print(num_of_paths_to_dest(1))
print(num_of_paths_to_dest(2))
print(num_of_paths_to_dest(3))
print(num_of_paths_to_dest(4))
print(num_of_paths_to_dest(5))
print(num_of_paths_to_dest(6))