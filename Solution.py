def num_of_paths_to_dest(n):
  dp = [1] * n
  
  for row in range(1, n):
    for col in range(row, n):
      if col > row:
        dp[col] += dp[col - 1]
  
  return dp[n-1]

print(num_of_paths_to_dest(4))
print(num_of_paths_to_dest(5))
print(num_of_paths_to_dest(6))