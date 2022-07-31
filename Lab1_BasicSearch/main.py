import BFS as b
import DFS as d
import Graph as g

if __name__ == '__main__':
    # BFS
    print("Co So Tri Tue Nhan Tao"
          "\nBai Tap Lap1: BFS va DFS setup"
          "\n Sinh Vien Pham Tuan Anh\n"
          "MSSV: 21880005\n")
    print("Phan 1:Thuat toan BFS")
    print("------------------------------------")
    b.RunBFS("Do thi 1:", g.Graph1, "A", "F")
    b.RunBFS("Do thi 2:", g.Graph2, "1", "11")
    b.RunBFS("Do thi 3:", g.Graph3, "s", "g")
    b.RunBFS("Do thi 4:", g.Graph4, "s", "g")
    b.RunBFS("Do thi 5:", g.Graph5, "A", "G")

    # DFS

    print("Phan 2:Thuat toan DFS ")
    print("------------------------------------")
    d.RunDFS("Do thi 1:", g.Graph1, "A", "F")
    d.RunDFS("Do thi 2:", g.Graph2, "1", "11")
    d.RunDFS("Do thi 3:", g.Graph3, "s", "g")
    d.RunDFS("Do thi 4:", g.Graph4, "s", "g")
    d.RunDFS("Do thi 5:", g.Graph5, "A", "G")