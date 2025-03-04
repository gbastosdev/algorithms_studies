# Explanation

Quick Sort is a highly efficient sorting algorithm and is based on partitioning of an array of data into smaller arrays. A large array is partitioned into two arrays, one of which holds values smaller than the specified value, say pivot, based on which the partition is made and another array holds values greater than the pivot value.

## How Quick Sort Works

1. **Choose a Pivot**: Pick an element from the array to be the pivot. This can be any element, but commonly the first, last, or middle element is chosen.
2. **Partitioning**: Rearrange the array so that all elements less than the pivot are on the left, all elements greater than the pivot are on the right. The pivot is now in its final position.
3. **Recursively Apply**: Recursively apply the above steps to the sub-array of elements with smaller values and the sub-array of elements with greater values.