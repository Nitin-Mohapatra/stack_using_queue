# 🧑‍💻 Stack Implementation Using Queues in Python  

This project demonstrates how to implement a **Stack (LIFO)** using **two Queues (FIFO)** in Python.  
It’s a common **coding interview question** and helps strengthen the understanding of **data structure transformations**.  

---

## 📖 Concept  

- **Stack** → Last In, First Out (LIFO)  
- **Queue** → First In, First Out (FIFO)  

By using **two queues**, we can simulate stack behavior:  

1. **Push(x)**  
   - Enqueue `x` into `q2`.  
   - Move all elements from `q1` into `q2`.  
   - Swap `q1` and `q2`.  

2. **Pop()**  
   - Dequeue from `q1`.  

3. **Top()**  
   - Peek the front element of `q1`.  

4. **Empty()**  
   - Check if `q1` is empty.  



⏱️ Time & Space Complexity

Push(x) → O(n)
(because we move all elements from q1 to q2)

Pop() → O(1)
(just dequeue from q1)

Top() → O(1)
(peek the front element of q1)

Empty() → O(1)
(check if q1 is empty)

Space Complexity → O(n)
(we store all elements in two queues)
