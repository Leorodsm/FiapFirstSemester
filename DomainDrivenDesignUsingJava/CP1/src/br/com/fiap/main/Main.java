package br.com.fiap.main;

import br.com.fiap.bean.DespesaFamiliar;
import java.util.Scanner;

// Aluno: Marcelo Alexandre dos Santos RM:565465
// Aluna: Poliana
// Aluno: Leonardo

public class Main {

    public static void main(String[] args) {

        DespesaFamiliar despesaFamiliar = new DespesaFamiliar();
        Scanner scan = new Scanner(System.in);

        int numeroDeMoradores;
        double rendaFamiliar, gastoComLuz, gastoComAgua, gastoComInternet, valorMensalidadeDaAcademia;

        System.out.println("\n---------------------------");
        System.out.println("CALCULADORA RENDA FAMILIAR");
        System.out.println("---------------------------");

        System.out.println("Por favor, insira o valor total de renda da sua família:");
        rendaFamiliar = scan.nextDouble();

        System.out.println("Digite quantos moradores residem em sua Casa: ");
        numeroDeMoradores = scan.nextInt();

        System.out.println("Digite o total a ser gasto na conta de Luz: ");
        gastoComLuz = scan.nextDouble();

        System.out.println("Digite o total a ser gasto na conta de Água: ");
        gastoComAgua = scan.nextDouble();

        System.out.println("Digite o total a ser gasto na conta de Internet: ");
        gastoComInternet = scan.nextDouble();

        System.out.println("Insira o valor da mensalidade da Academia: ");
        valorMensalidadeDaAcademia = scan.nextDouble();

        despesaFamiliar.rendaFamiliar = rendaFamiliar;
        despesaFamiliar.numeroDeMoradores = numeroDeMoradores;
        despesaFamiliar.gastoComLuz = gastoComLuz;
        despesaFamiliar.gastoComAgua = gastoComAgua;
        despesaFamiliar.gastoComInternet = gastoComInternet;
        despesaFamiliar.valorMensalidadeDaAcademia = valorMensalidadeDaAcademia;


        System.out.println("---------------------------------------");
        System.out.printf("A Renda Total da família é de: R$ %.3f\nO total de gastos da família foi: R$ %.3f\nE a Renda Familiar Liquida foi: R$ %.3f\n",
                despesaFamiliar.rendaFamiliar, despesaFamiliar.calcularTotalDeDespesas(), despesaFamiliar.calcularRendaFamiliarLiquida());
        System.out.println("---------------------------------------");


    }

}
