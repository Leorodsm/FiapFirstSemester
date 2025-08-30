package br.com.fiap.bean;

import java.util.Date;
import java.util.Scanner;

public class SessaoTeleconsulta {
    private String idSessao;
    private Date dtDisponivel;
    private Date dtHoraAgendado;
    private String dsLinkVideoConferencia;
    private char stStatus;
    private Paciente paciente;  // Associação com Paciente
    private Profissional profissional;  // Associação com Profissional

    // ... (getters e setters existentes)

    // Adicionar getters e setters para paciente e profissional
    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

    public Profissional getProfissional() {
        return profissional;
    }

    public void setProfissional(Profissional profissional) {
        this.profissional = profissional;
    }

    public void cadastrarConsulta() {
        Scanner scanner = new Scanner(System.in);
        boolean continuar = true;

        while (continuar) {
            System.out.println("\n--- AGENDAMENTO DE CONSULTA ---");
            System.out.println("DATAS DISPONÍVEIS:");
            System.out.println("1- 28/05 as 15h20");
            System.out.println("2- 03/06 as 10h15");
            System.out.println("3- 07/06 as 19h20");
            System.out.println("4- 11/06 as 8h10");
            System.out.println("5- 17/06 as 10h10");
            System.out.print("Escolha uma data (1-5): ");

            try {
                int escolha = scanner.nextInt();

                if (escolha < 1 || escolha > 5) {
                    System.out.println("ERRO: Opção inválida! Digite um número entre 1 e 5.");
                } else {
                    String[] datas = {
                            "28/05 as 15:20 da TARDE",
                            "03/06 as 10:15 da MANHÃ",
                            "07/06 as 19:20 da NOITE",
                            "11/06 as 08:10 da MANHÃ",
                            "17/06 as 10:10 da MANHÃ"
                    };

                    System.out.println("\nHorário AGENDADO para " + datas[escolha-1] + "!");
                    System.out.println("No dia da consulta você receberá um link para acessar a TELECONSULTA!");
                }
            } catch (Exception e) {
                System.out.println("ERRO: Digite apenas números de 1 a 5!");
                scanner.next();
                continue;
            }

            System.out.print("\nDeseja agendar outra consulta? (S/N): ");
            char resposta = scanner.next().charAt(0);
            continuar = (resposta == 'S' || resposta == 's');
        }
    }
}