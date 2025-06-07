import sys

def process_numbers():
    try:
        with open('data_1.txt', 'w') as f1:
            f1.write('-5 10 -3 8 15 -7 20')
        with open('data_2.txt', 'w') as f2:
            f2.write('12 -8 6 -5 18 10 -3')

        with open('data_1.txt') as f1, open('data_2.txt') as f2:
            nums1 = list(map(int, f1.read().split()))
            nums2 = list(map(int, f2.read().split()))

        common = len(set(nums1) & set(nums2))
        even1 = len([x for x in nums1 if x % 2 == 0])
        odd2 = len([x for x in nums2 if x % 2 != 0])

        with open('result_numbers.txt', 'w') as f3:
            f3.write(f"{nums1}\n{nums2}\n")
            f3.write(f"{len(nums1)} {len(nums2)}\n")
            f3.write(f"{common}\n")
            f3.write(f"{even1}\n")
            f3.write(f"{odd2}\n")

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")

if __name__ == "__main__":
    process_numbers()