
import n1_crack
import n2_crack
import n1_edge_crack
import replicate_cell

if __name__ == "__main__":
    print()
    print("============================== Gerando Estruturas ==============================\n")
    n1_crack.run('x')
    n1_crack.run('y')
    n1_edge_crack.run()
    n2_crack.run('y')
    replicate_cell.run()
    print()
    print("\033[1;32m" + "============================== Estruturas replicadas ===========================" + "\033[0m")