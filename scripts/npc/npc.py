# npc.py
### agora precisa fazer a integração de atualizar o progresso da historia no mestre.
### verificador de progresso da historia pra chegar em algum ponto EXPLODDIR
import subprocess
from montadora_npc import NPCMissionState

def run_planner(domain_file, problem_file):
    """
    Chama o planejador Madagascar para o NPC com os arquivos dados.
    Retorna a saída do planejador como string.
    """
    try:
        command = ["MADAGASCAR/MpC", domain_file, problem_file]
        output = subprocess.check_output(command).decode("utf-8")
        return output
    except subprocess.CalledProcessError as e:
        return f"Erro ao chamar o planejador: {e.output.decode('utf-8')}"

def main():
    state = NPCMissionState()
    domain_file = "pddls/npc/domain_missao.pddl"      
    problem_file = "pddls/npc/problema_missao_atual.pddl"  

    print("Iniciando interação com o NPC para montar a missão.")
    while state.mission_active:
        state.print_state()
        state.export_problem(problem_file)
        plan = run_planner(domain_file, problem_file)
        print("Plano gerado pelo Madagascar para o NPC:")
        print(plan)
        print("--------------------------------------------------\n")
        
        actions = state.available_actions()
        if not actions:
            print("Nenhuma ação disponível para o NPC. Interação encerrada.")
            break
        
        print("Ações disponíveis para o NPC:")
        for idx, act in enumerate(actions):
            print(f"  {idx+1}. {act}")
        choice = input("Escolha uma ação para o NPC (digite o número): ")
        
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(actions):
                print("Opção inválida. Tente novamente.\n")
                continue
            chosen_action = actions[index]
            state.update_action(chosen_action)
        except ValueError:
            print("Digite um número válido.\n")
            continue
        
        # Se a ação escolhida for "finalizar_missao", encerra a interação
        if chosen_action == "finalizar_missao":
            break
        
        input("\nPressione Enter para continuar...\n")
    
    print("Interação com o NPC encerrada.")
    state.print_state()

if __name__ == "__main__":
    main()
