package br.com.fiap.main;

import java.util.Scanner;

public class MainEx1 {

    // Exercício 1

    public static void main(String[] args) {
        float prova1;
        float prova2;
        float resultado;

        Scanner scan;

        try {
            scan = new Scanner(System.in);

            System.out.println("Digite a nota 1: ");
            prova1 = scan.nextFloat();

            System.out.println("Digite a nota 2: ");
            prova2 = scan.nextFloat();

            resultado = (prova1 + prova2 ) / 2;

            System.out.printf("A média é "+resultado);


        } catch (Exception e) {
            System.out.println("Deu erro");
        }
    }
}
