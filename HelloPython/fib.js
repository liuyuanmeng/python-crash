function fibonacci(n) {
  const sequence = [0, 1]
  for (let i = 2; i < n; i++){
    const nextNum = sequence[i - 1] + sequence[i - 2]
    sequence.push(nextNum)

  }
  return sequence
  
}

// Example usage:
var fibSequence = fibonacci(10)
console.log(fibSequence) // Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


