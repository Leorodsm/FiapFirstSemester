package br.com.fiap.main;

import br.com.fiap.bean.Pessoa;

import java.util.Scanner;

public class MainV2 {
    public static void main(String[] args) {
        Pessoa pessoa1;
        String nome;
        int anoNascimento;

        Scanner scan;

        try {
            scan = new Scanner(System.in);

            System.out.println("Digite seu nome e ano de nascimento: ");
            nome = scan.nextLine();
            anoNascimento = scan.nextInt();

            pessoa1 = new Pessoa(nome, anoNascimento);
            int idadePessoa1 = pessoa1.calcularIdade(2025);

        } catch (Exception e) {
            System.out.println("Nome ou ano de nascimento inválido(s)");
        }



    }
}
