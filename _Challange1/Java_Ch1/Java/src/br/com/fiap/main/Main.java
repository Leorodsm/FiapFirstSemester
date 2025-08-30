package br.com.fiap.main;

import br.com.fiap.bean.Faq;
import br.com.fiap.bean.Paciente;
import br.com.fiap.bean.SessaoTeleconsulta;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean cadastrado = false;
        Paciente paciente = null;

        System.out.println("=== BEM-VINDO AO SISTEMA DE TELECONSULTA ===");

        // Fluxo de cadastro
        while (!cadastrado) {
            System.out.println("\n[1] Cadastrar como Paciente");
            System.out.println("[2] Já sou cadastrado");
            System.out.print("Escolha: ");

            int opcao = scanner.nextInt();
            scanner.nextLine();

            if (opcao == 1) {
                paciente = new Paciente();
                boolean dadosValidos = false;

                while (!dadosValidos) {
                    // Nome
                    System.out.print("Nome completo: ");
                    String nome = scanner.nextLine();
                    if (nome == "") {  // Verifica se está vazio
                        System.out.println("Nome não pode ser vazio!");
                        continue;
                    }
                    paciente.setNmCompleto(nome);

                    // CPF
                    System.out.print("CPF (11 dígitos): ");
                    String cpf = scanner.nextLine();
                    int contador = 0;
                    for (int i = 0; i < cpf.length(); i++) {  // Conta dígitos sem usar .length()
                        contador++;
                    }
                    if (contador != 11) {
                        System.out.println("CPF deve ter 11 dígitos!");
                        continue;
                    }
                    paciente.setNrCpf(cpf);

                    // Sexo
                    System.out.print("Sexo (M/F): ");
                    String sexo = scanner.nextLine();

                    paciente.setDsSexoBiologico(sexo.charAt(0));

                    // Data Nascimento
                    System.out.print("Data nascimento (DDMMAAAA): ");
                    String data = scanner.nextLine();
                    contador = 0;
                    for (int i = 0; i < data.length(); i++) {
                        contador++;
                    }
                    if (contador != 8) {
                        System.out.println("Digite 8 dígitos (DDMMAAAA)!");
                        continue;
                    }

                    dadosValidos = true;
                    System.out.println("\nCadastro realizado!");
                    cadastrado = true;
                }

            } else if (opcao == 2) {
                System.out.print("E-mail cadastrado: ");
                String email = scanner.nextLine();
                if (email != "") {  // Verifica se não está vazio
                    cadastrado = true;
                }
            } else {
                System.out.println("Opção inválida!");
            }
        }

        // Menu principal
        boolean executando = true;
        while (executando) {
            System.out.println("\n=== MENU ===");
            System.out.println("[1] Agendar Consulta");
            System.out.println("[2] Cadastrar Dúvida");
            System.out.println("[3] Sair");
            System.out.print("Escolha: ");

            int escolha = scanner.nextInt();
            scanner.nextLine(); // Limpar buffer

            if (escolha == 1) {
                new SessaoTeleconsulta().cadastrarConsulta();
            } else if (escolha == 2) {
                new Faq().cadastrarFAQ();
            } else if (escolha == 3) {
                executando = false;
                System.out.println("Sistema encerrado.");
            } else {
                System.out.println("Opção inválida!");
            }
        }
        scanner.close();
    }
}