import java.util.*;

// Do not edit the class below except for the buildHeap,
// siftDown, siftUp, peek, remove, and insert methods.
// Feel free to add new properties and methods to the class.
class Program {
    static class MinHeap {
        List<Integer> heap = new ArrayList<Integer>();

        public MinHeap(List<Integer> array) {
            heap = buildHeap(array);
        }

        public List<Integer> buildHeap(List<Integer> array) {
            // Write your code here.
            // return new ArrayList<Integer>();
            int n = array.size();
            for (int i = getParentIndex(n - 1); i >= 0; i--) {
                siftDown(i, n - 1, array);
            }
            return array;
        }

        private int getParentIndex(int currentIdx) {
            int parentIndex = Math.floorDiv(currentIdx - 1, 2);
            return parentIndex;
        }

        private ArrayList<Integer> getChildIndices(int parentIndex) {
            ArrayList<Integer> childIndices = new ArrayList<Integer>();
            childIndices.add(parentIndex * 2 + 1);
            childIndices.add(parentIndex * 2 + 2);
            return childIndices;
        }

        private int getMinChildIndex(int parentIndex, List<Integer> heap) {
            ArrayList<Integer> childIndices = getChildIndices(parentIndex);
            int n = heap.size();
            if (childIndices.get(0) >= n) {
                return -1;
            } else if (childIndices.get(1) >= n) {
                if (heap.get(childIndices.get(0)) < heap.get(parentIndex)) {
                    return childIndices.get(0);
                } else {
                    return -1;
                }
            }
            int parent = heap.get(parentIndex);
            int leftChild = heap.get(childIndices.get(0));
            int rightChild = heap.get(childIndices.get(1));

            if (parent < leftChild && parent < rightChild)
                return -1;
            if (leftChild < rightChild)
                return childIndices.get(0);
            return childIndices.get(1);
        }

        private void swap(int i, int j, List<Integer> heap) {
            int t = heap.get(i);
            heap.set(i, heap.get(j));
            heap.set(j, t);
        }

        public void siftDown(int currentIdx, int endIdx, List<Integer> heap) {
            int minChildIndex = getMinChildIndex(currentIdx, heap);
            if (minChildIndex == -1 || minChildIndex > endIdx)
                return;
            swap(currentIdx, minChildIndex, heap);
            siftDown(minChildIndex, endIdx, heap);

        }

        public void siftUp(int currentIdx, List<Integer> heap) {
            int parentIndex = getParentIndex(currentIdx);
            if (parentIndex >= 0 && heap.get(currentIdx) < heap.get(parentIndex)) {
                swap(currentIdx, parentIndex, heap);
                siftUp(parentIndex, heap);
            }
        }

        public int peek() {
            return this.heap.get(0);
        }

        public int remove() {
            int n = this.heap.size();
            swap(0, n - 1, heap);
            int removedElement = this.heap.remove(n - 1);
            siftDown(0, n - 1, this.heap);
            return removedElement;
        }

        public void insert(int value) {
            heap.add(value);
            int n = heap.size();
            siftUp(n - 1, heap);
        }
    }
}
