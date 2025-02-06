# montador_npc.py

class NPCMissionState:
    def __init__(self):
        # Estado para a missão m1
        self.mission_active = True   # Missão m1 está ativa
        self.clientes_contatados = 0
        self.progresso_historia = 0
        self.fatos_obtidos = set()   
        self.fatos_contados = set()
        self.recompensa_entregue = False

    def available_actions(self):
        """
        Retorna uma lista de strings com as ações disponíveis para o NPC.
        """
        actions = []
        # Se ainda não contatou 3 clientes, pode falar com um cliente
        if self.clientes_contatados < 3:
            actions.append("falar_com_cliente")
        # Se já falou com algum cliente e ainda não obteve o fato f1, pode obter o fato
        if self.clientes_contatados > 0 and "f1" not in self.fatos_obtidos:
            actions.append("obter_fato")
        # Se o fato foi obtido e ainda não contado, pode contar o fato
        if "f1" in self.fatos_obtidos and "f1" not in self.fatos_contados:
            actions.append("contar_fato")
        # Se o fato foi contado e a recompensa ainda não foi entregue, pode entregar a recompensa
        if "f1" in self.fatos_contados and not self.recompensa_entregue:
            actions.append("entregar_recompensa")
        # Sempre pode progredir a história se a missão estiver ativa
        if self.mission_active:
            actions.append("progredir_historia")
        # Se todas as metas foram atingidas, permite finalizar a missão
        if (self.clientes_contatados >= 3 and "f1" in self.fatos_obtidos and
            "f1" in self.fatos_contados and self.recompensa_entregue and
            self.progresso_historia >= 3):
            actions.append("finalizar_missao")
        return actions

    def update_action(self, action):
        """
        Atualiza o estado do NPC conforme a ação escolhida.
        """
        if action == "falar_com_cliente":
            self.clientes_contatados += 1
            print(f"NPC: Falou com um cliente. Total: {self.clientes_contatados}")
        elif action == "obter_fato":
            self.fatos_obtidos.add("f1")
            print("NPC: Obteve o fato f1.")
        elif action == "contar_fato":
            self.fatos_contados.add("f1")
            print("NPC: Contou o fato f1 para rowan.")
        elif action == "entregar_recompensa":
            self.recompensa_entregue = True
            print("NPC: Entregou a recompensa x.")
        elif action == "progredir_historia":
            self.progresso_historia += 3
            print(f"NPC: Progrediu a história em +3. Total: {self.progresso_historia}")
        elif action == "finalizar_missao":
            self.mission_active = False
            print("NPC: Missão finalizada com sucesso!")
        else:
            print("Ação NPC não reconhecida.")

    def print_state(self):
        print("\n--- Estado NPC ---")
        print(f"Missão ativa: {self.mission_active}")
        print(f"Clientes contatados: {self.clientes_contatados}")
        print(f"Progresso da história: {self.progresso_historia}")
        print(f"Fatos obtidos: {self.fatos_obtidos}")
        print(f"Fatos contados: {self.fatos_contados}")
        print(f"Recompensa entregue: {self.recompensa_entregue}")
        print("------------------\n")

    def export_problem(self, filename="pddls/npc/problema_missao_atual.pddl"):
        """
        Exporta um arquivo PDDL que reflete o estado atual da missão NPC.
        """
        pddl_text = ";; Problema NPC gerado automaticamente\n"
        pddl_text += "(define (problem missao1)\n"
        pddl_text += "  (:domain missao)\n"
        pddl_text += "  (:objects\n"
        pddl_text += "    m1 - missao\n"
        pddl_text += "    c1 c2 c3 - cliente\n"
        pddl_text += "    f1 - fato\n"
        pddl_text += "    rowan - npc\n"
        pddl_text += "    x - recompensa\n"
        pddl_text += "  )\n"
        pddl_text += "  (:init\n"
        pddl_text += "    (missao-ativa m1)\n"
        pddl_text += f"    (= (clientes-contatados m1) {self.clientes_contatados})\n"
        pddl_text += f"    (= (progresso-historia m1) {self.progresso_historia})\n"
        
        pddl_text += "    (fornece c3 f1)\n"
        if "f1" in self.fatos_obtidos:
            pddl_text += "    (fato-obtido m1 f1)\n"
        if "f1" in self.fatos_contados:
            pddl_text += "    (fato-contado m1 f1 rowan)\n"
        if self.recompensa_entregue:
            pddl_text += "    (recompensa-entregue m1 x)\n"
        pddl_text += "  )\n"
        pddl_text += "  (:goal (and\n"
        pddl_text += "    (>= (clientes-contatados m1) 3)\n"
        pddl_text += "    (fato-obtido m1 f1)\n"
        pddl_text += "    (fato-contado m1 f1 rowan)\n"
        pddl_text += "    (recompensa-entregue m1 x)\n"
        pddl_text += "    (>= (progresso-historia m1) 3)\n"
        pddl_text += "  ))\n"
        pddl_text += ")\n"

        with open(filename, "w") as f:
            f.write(pddl_text)
        print(f"Arquivo de problema NPC atualizado salvo em '{filename}'.")

