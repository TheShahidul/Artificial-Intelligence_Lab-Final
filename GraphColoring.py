class GraphColoring:
    def __init__(self):
        self.v = 0
        self.numOfColors = 0
        self.color = []
        self.graph = []
        self.states = []

    def graphColor(self, g, noc, states):
        self.v = len(g)
        self.numOfColors = noc
        self.color = [0] * self.v
        self.graph = g
        self.states = states
        try:
            self.solve(0)
            print("No solution")
        except:
            print("\nSolution exists")
            self.display()

    def solve(self, v):
        if v == self.v:
            raise Exception("Solution found")
        for c in range(1, self.numOfColors + 1):
            if self.isPossible(v, c):
                self.color[v] = c
                self.solve(v + 1)
                self.color[v] = 0

    def isPossible(self, v, c):
        for i in range(self.v):
            if self.graph[v][i] == 1 and c == self.color[i]:
                return False
        return True

    def display(self):
        textcolor = ["", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE", "PINK", "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"]
        print("\ncolors :", end=" ")
        for i in range(self.v):
            print(self.states[i].capitalize() + "=\"" + textcolor[self.color[i]], end="\"; ")

    @staticmethod
    def main():
        print("Graph Coloring Algorithm Test\n")
        gc = GraphColoring()
        graph = []
        states = []

        file_path = r'"D:\Spring 2024 [7th Semester]\CSE316_Artificial Intelligence Lab\lab report 5\graph-sample.txt"'  # Update file path here
        mode = "r"  # for read mode in file
        file = open(file_path, mode)

        no_of_vertex = int(file.readline().strip())
        print(no_of_vertex)
        no_of_colors = int(file.readline().strip())
        print(no_of_colors)

        file.readline()  # pointer to nextline

        line = file.readline().strip()  # first state

        while line:
            states.append(line)
            line = file.readline().strip()

        for line in file:
            elements = line.strip().split()
            adj_list = [int(element) for element in elements]
            graph.append(adj_list)
        file.close()
        print(states)
        print(graph)
        gc.graphColor(graph, no_of_colors, states)

if __name__ == "__main__":
    GraphColoring.main()
