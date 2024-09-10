import java.util.Arrays;

public class 列表实现 {
	class MyList {
		private int[] arr; // 数组（存储列表元素）
		private int capacity = 10; // 数组容量
		private int size = 0; // 列表元素个数(元素数量或者长度)
		private int extendRatio = 2; // 每次列表扩容的倍数

		// 构造方法
		public MyList() {
			arr = new int[capacity];
		}

		// 获取列表长度
		public int size() {
			return size;
		}

		// 获取列表容量
		public int capacity() {
			return capacity;
		}

		// 访问元素
		public int get(int index) {
			// 判断索引是否越界
			if (index < 0 || index >= size)
				throw new IndexOutOfBoundsException("索引越界");
			return arr[index];
		}

		// 更新元素
		public void set(int index, int num) {
			if (index < 0 || index >= size)
				throw new IndexOutOfBoundsException("索引越界");
			arr[index] = num;
		}

		// 在尾部添加元素
		public void add(int num) {
			// 判断是否需要扩容
			if (size == capacity())
				extendCapacity();
			arr[size] = num;
			size++;
		}

		// 在中间插入元素
		public void insert(int index, int num) {
			if (index < 0 || index > size)
				throw new IndexOutOfBoundsException("索引越界");
			// 判断是否需要扩容
			if (size == capacity())
				extendCapacity();
			// 将index后的元素向后移动一位
			for (int j = size - 1; j >= index; j--) {
				arr[j + 1] = arr[j];
			}
			arr[index] = num;
			// 更新size
			size++;
		}

		// 删除元素
		public int remove(int index) {
			if (index < 0 || index >= size)
				throw new IndexOutOfBoundsException("索引越界");
			int num = arr[index];
			// 将index后的元素向前移动一位
			for (int j = index; j < size - 1; j++) {
				arr[j] = arr[j + 1];
			}
			// 更新size
			size--;
			return num;
		}

		// 扩容
		public void extendCapacity() {
			// 新建一个长度为原数组长度的extendRatio倍的数组，并且将原数组的元素复制到新数组中
			arr = Arrays.copyOf(arr, capacity() * extendRatio);
			// 更新容量
			capacity = arr.length;
		}

		// 将列表转化为数组
		public int[] toArray() {
			int size = size();
			// 仅转换有效长度范围内的列表元素
			int[] arr = new int[size];
			for (int i = 0; i < size; i++) {
				arr[i] = get(i);
			}
			return arr;
		}
	}
}