import random

class ProblemState:
    def __init__(self):
        # Fases: "p1" = ciclo 0; "p2" = ciclo 1; "p3" = ciclo 2; "p4" = fim (objetivo alcançado)
        self.phase = "p1"
        # Ciclo 0
        self.c0_started = False
        self.diario = False         # True se o diário foi pego
        self.cenario = False          # True se o cenário foi arrumado
        self.c0_finalizado = False
        self.good_c0 = False        # Será True se ambos diário e cenário forem feitos
        
        # Ciclo 1
        self.c1_started = False
        self.mission1 = False
        self.mission2 = False
        self.c1_finalizado = False
        
        # Ciclo 2
        self.c2_started = False
        self.mission3 = False
        self.mission4 = False
        self.c2_finalizado = False

    def available_actions(self):
        """
        Retorna uma lista de strings com as ações disponíveis, de acordo com self.phase.
        """
        if self.phase == "p1":  # Ciclo 0: fase obrigatória de pegar o diário e arrumar o cenário
            actions = []
            if not self.c0_started:
                actions.append("iniciar_c0")
            else:
                if not self.diario:
                    actions.append("pegar_diario")
                if not self.cenario:
                    actions.append("arrumar_cenario")
                # Permite finalizar o ciclo 0 mesmo que falte algo, mas finalização "boa" só se ambos estiverem feitos
                if self.diario and self.cenario:
                    actions.append("finalizar_c0_good")
                else:
                    actions.append("finalizar_c0_bad")
            return actions

        elif self.phase == "p2":  # Ciclo 1: ações de missão
            actions = []
            if not self.c1_started:
                actions.append("iniciar_c1")
            else:
                # Para mission1: escolha aleatória com pesos
                if not self.mission1:
                    opts1 = ["aceitar_mission1_low", "aceitar_mission1_high"]
                    weights1 = [0.8, 0.2] if self.good_c0 else [0.2, 0.8]
                    chosen1 = random.choices(opts1, weights=weights1, k=1)[0]
                    actions.append(chosen1)
                # Para mission2: escolha aleatória com pesos
                if not self.mission2:
                    opts2 = ["aceitar_mission2_low", "aceitar_mission2_high"]
                    weights2 = [0.8, 0.2] if self.good_c0 else [0.2, 0.8]
                    chosen2 = random.choices(opts2, weights=weights2, k=1)[0]
                    actions.append(chosen2)
                
                actions.append("finalizar_c1")
            return actions

        elif self.phase == "p3":  # Ciclo 2: ações de missão
            actions = []
            if not self.c2_started:
                actions.append("iniciar_c2")
            else:
                opts = []
                if not self.mission3:
                    opts_m3 = ["aceitar_mission3_low", "aceitar_mission3_high"]
                    weights_m3 = [0.8, 0.2] if self.mission1 else [0.2, 0.8]
                    opts.append(random.choices(opts_m3, weights=weights_m3, k=1)[0])
                if not self.mission4:
                    opts_m4 = ["aceitar_mission4_low", "aceitar_mission4_high"]
                    weights_m4 = [0.8, 0.2] if self.mission2 else [0.2, 0.8]
                    opts.append(random.choices(opts_m4, weights=weights_m4, k=1)[0])
                random.shuffle(opts)
                actions.extend(opts)
                # Permite finalizar o ciclo 2 sempre, mesmo que nenhuma missão tenha sido realizada
                actions.append("finalizar_c2")
            return actions

        elif self.phase == "p4":
            return []  # Jogo terminado

        else:
            return []

    def update_action(self, action):
        """
        Atualiza o estado conforme a ação escolhida.
        """
        if action == "iniciar_c0":
            self.c0_started = True
            print("Ciclo 0 iniciado.")
        elif action == "pegar_diario":
            self.diario = True
            print("Você pegou o diário.")
        elif action == "arrumar_cenario":
            self.cenario = True
            print("Você arrumou o cenário.")
        elif action == "finalizar_c0_good":
            if self.diario and self.cenario:
                self.good_c0 = True
                self.c0_finalizado = True
                self.phase = "p2"
                print("Ciclo 0 finalizado com sucesso!")
            else:
                print("Não foi possível finalizar o ciclo 0 como 'bom'.")
        elif action == "finalizar_c0_bad":
            self.c0_finalizado = True
            self.phase = "p2"
            print("Ciclo 0 finalizado, mas sem sucesso ideal (diário e/ou cenário faltaram).")
        elif action == "iniciar_c1":
            self.c1_started = True
            print("Ciclo 1 iniciado.")
        elif action in ["aceitar_mission1_low", "aceitar_mission1_high"]:
            self.mission1 = True
            if "low" in action:
                print("Você aceitou a Missão 1 (custo baixo).")
            else:
                print("Você aceitou a Missão 1 (custo alto).")
        elif action in ["aceitar_mission2_low", "aceitar_mission2_high"]:
            self.mission2 = True
            if "low" in action:
                print("Você aceitou a Missão 2 (custo baixo).")
            else:
                print("Você aceitou a Missão 2 (custo alto).")
        elif action == "finalizar_c1":
            self.c1_finalizado = True
            self.phase = "p3"
            if self.mission1 or self.mission2:
                print("Ciclo 1 finalizado com algumas missões realizadas.")
            else:
                print("Ciclo 1 finalizado sem realizar nenhuma missão.")
        elif action == "iniciar_c2":
            self.c2_started = True
            print("Ciclo 2 iniciado.")
        elif action in ["aceitar_mission3_low", "aceitar_mission3_high"]:
            self.mission3 = True
            if "low" in action:
                print("Você aceitou a Missão 3 (custo baixo).")
            else:
                print("Você aceitou a Missão 3 (custo alto).")
        elif action in ["aceitar_mission4_low", "aceitar_mission4_high"]:
            self.mission4 = True
            if "low" in action:
                print("Você aceitou a Missão 4 (custo baixo).")
            else:
                print("Você aceitou a Missão 4 (custo alto).")
        elif action == "finalizar_c2":
            self.c2_finalizado = True
            self.phase = "p4"
            if self.mission3 or self.mission4:
                print("Ciclo 2 finalizado com missões realizadas. Jogo encerrado!")
            else:
                print("Ciclo 2 finalizado sem realizar nenhuma missão. Jogo encerrado!")
        else:
            print("Ação não reconhecida.")

    def print_state(self):
        """Exibe o estado atual (para visualização)."""
        print("\n--- Estado Atual ---")
        print(f"Fase: {self.phase}")
        print(f"Ciclo 0: iniciado={self.c0_started}, diário={self.diario}, cenário={self.cenario}, finalizado={self.c0_finalizado}, good_c0={self.good_c0}")
        print(f"Ciclo 1: iniciado={self.c1_started}, mission1={self.mission1}, mission2={self.mission2}, finalizado={self.c1_finalizado}")
        print(f"Ciclo 2: iniciado={self.c2_started}, mission3={self.mission3}, mission4={self.mission4}, finalizado={self.c2_finalizado}")
        print("---------------------\n")

    def export_problem(self, filename="pddls/mestre/problema_mestre_atual.pddl"):
        """
        Exporta um arquivo PDDL com base no estado atual.
        """
        pddl_text = ";; Problema gerado automaticamente\n"
        pddl_text += "(define (problem problema_mestre)\n"
        pddl_text += "  (:domain jogo-custo)\n"
        pddl_text += "  (:objects \n    c0 c1 c2 - ciclo\n    mission1 mission2 mission3 mission4 - mission\n    p1 p2 p3 p4 - phase\n  )\n"
        pddl_text += "  (:init\n"
        pddl_text += f"    (current-phase {self.phase})\n"
        if self.diario:
            pddl_text += "    (diario-preso)\n"
        if self.cenario:
            pddl_text += "    (cenario-arrumado)\n"
        if self.good_c0:
            pddl_text += "    (good-c0)\n"
        if self.mission1:
            pddl_text += "    (mission-done mission1)\n"
        if self.mission2:
            pddl_text += "    (mission-done mission2)\n"
        if self.mission3:
            pddl_text += "    (mission-done mission3)\n"
        if self.mission4:
            pddl_text += "    (mission-done mission4)\n"
        pddl_text += "  )\n"
        pddl_text += "  (:goal (current-phase p4))\n"
        pddl_text += ")\n"

        with open(filename, "w") as f:
            f.write(pddl_text)
        print(f"Arquivo de problema atualizado salvo em '{filename}'.")

