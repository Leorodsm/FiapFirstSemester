package br.com.fiap.main;

import java.util.Scanner;

public class MainEx2 {
    public static void main(String[] args) {
        int anoAtual;
        int anoNascimento;
        int idade;

        Scanner scan;

        try {
            scan = new Scanner(System.in);

            System.out.println("Digite o ano atual: ");
            anoAtual = scan.nextInt();

            System.out.println("Digite o ano em que nasceu");
            anoNascimento = scan.nextInt();

            idade = anoAtual - anoNascimento;

            System.out.println("Sua idade é "+idade);

        } catch (Exception e) {
            System.out.println("Deu erro.");
        }
    }
}
