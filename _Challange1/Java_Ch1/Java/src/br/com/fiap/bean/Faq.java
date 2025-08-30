package br.com.fiap.bean;

import java.util.Scanner;

public class Faq extends Usuario {
    private String idFaq;
    private String dsPergunta;
    private String dsResposta;

    // ... (getters e setters existentes)

    public void cadastrarFAQ() {
        Scanner scanner = new Scanner(System.in);
        boolean continuar = true;

        while (continuar) {
            System.out.println("\n--- CADASTRO DE DÚVIDA ---");

            System.out.print("Digite o seu e-mail: ");
            String email = scanner.nextLine();

            System.out.print("Digite a sua dúvida: ");
            String duvida = scanner.nextLine();

            System.out.println("\nDúvida cadastrada! Você receberá uma resposta por e-mail.");

            System.out.print("\nDeseja cadastrar outra dúvida? (sim/não): ");
            String resposta = scanner.nextLine();

            if (resposta.equals("não")) {
                continuar = false;
            }
        }
    }
}