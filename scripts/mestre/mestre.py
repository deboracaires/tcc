import subprocess
from montadora_mestre import ProblemState

def run_planner(domain_file, problem_file):
    """
    Chama o planejador Madagascar com os arquivos de domínio e problema.
    Retorna a saída (o plano gerado) como uma string.
    """
    try:
        command = ["MADAGASCAR/MpC", domain_file, problem_file]
        output = subprocess.check_output(command).decode("utf-8")
        return output
    except subprocess.CalledProcessError as e:
        return f"Erro ao chamar o planejador: {e.output.decode('utf-8')}"

def main():
    state = ProblemState()
   
    domain_file = "pddls/mestre/dominio_mestre.pddl"
    problem_file = "pddls/mestre/problema_mestre_atual.pddl"

    print("Bem-vindo ao jogo mestre (interface de texto)!")
    print("Você deverá tomar decisões que atualizam o problema do jogo.")
    print("Após cada escolha, o planejador será chamado para gerar um plano com base no estado atual.\n")

    while state.phase != "p4":
        state.print_state()
        state.export_problem(problem_file)
        
        # Chama o planejador e exibe o plano gerado
        plan = run_planner(domain_file, problem_file)
        print("Plano gerado pelo Madagascar:")
        print(plan)
        print("--------------------------------------------------\n")
        
        # Exibe as opções disponíveis para o mestre.
        # (A opção 0 para chamar o NPC também pode ser mantida se desejar; veja a integração abaixo.)
        print("Ações disponíveis:")
        actions = state.available_actions()
       
        for idx, act in enumerate(actions):
            print(f"  {idx+1}. {act}")
        
        choice = input("Escolha uma ação (digite o número): ")
        if choice.strip() == "0":
            print("Chamando o NPC para montar a missão...\n")
            subprocess.call(["python3", "scripts/npc/npc.py"])
            input("\nNPC finalizou sua execução. Pressione Enter para retomar o jogo mestre...")
            continue

        try:
            index = int(choice) - 1
            if index < 0 or index >= len(actions):
                print("Opção inválida. Tente novamente.\n")
                continue
            chosen_action = actions[index]
            state.update_action(chosen_action)
            # Se o jogador aceitou uma missão, chama automaticamente o NPC para montar/executar os passos.
            if chosen_action.startswith("aceitar_mission"):
                print("\nMissão aceita! Chamando o NPC para montar e executar a missão...")
                subprocess.call(["python3", "scripts/npc/npc.py"])
                input("\nNPC finalizou sua execução. Pressione Enter para retomar o jogo mestre...")
        except ValueError:
            print("Digite um número válido.\n")
            continue

        input("\nPressione Enter para continuar...\n")
    
    if state.phase == "p4":
        print("Parabéns! Você concluiu o jogo mestre.")
        state.print_state()
    else:
        print("O jogo foi interrompido.")

if __name__ == "__main__":
    main()
