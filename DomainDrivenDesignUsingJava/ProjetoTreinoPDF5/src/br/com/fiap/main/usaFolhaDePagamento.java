package br.com.fiap.main;

import br.com.fiap.bean.FolhaDePagamento;

import java.util.Scanner;

public class usaFolhaDePagamento {
    public static void main(String[] args) {
        FolhaDePagamento folhaDePagamento = new FolhaDePagamento();

        Scanner scan;

        try {
            scan = new Scanner(System.in);

            System.out.println("Digite o salário bruto: ");
            folhaDePagamento.salarioBruto = scan.nextDouble();

            System.out.println("Digite o número de dependentes: ");
            folhaDePagamento.numeroDeDependentes = scan.nextInt();

            System.out.println("Digite o valor do plano de saúde: ");
            folhaDePagamento.valorPlanoDeSaude = scan.nextDouble();

            System.out.println("Valor do desconto do INSS: ");
            folhaDePagamento.descontoINSS = scan.nextDouble();

            System.out.printf("Salário bruto: %.2f\nDependentes: %d\nValor Plano de Saúde: %.2f\nDesconto INSS: %.1f%%\nSalário Líquido: %.2f\n",folhaDePagamento.salarioBruto, folhaDePagamento.numeroDeDependentes,folhaDePagamento.valorPlanoDeSaude, folhaDePagamento.descontoINSS, folhaDePagamento.calcularSalarioLiquido());
        } catch (Exception e) {
            System.out.println("Deu erro!");
        }


    }
}
