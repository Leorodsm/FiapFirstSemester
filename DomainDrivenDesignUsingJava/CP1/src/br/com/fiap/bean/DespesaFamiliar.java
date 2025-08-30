package br.com.fiap.bean;

// Aluno: Marcelo Alexandre dos Santos RM:565465
// Aluna: Poliana
// Aluno: Leonardo

public class DespesaFamiliar {

    public double rendaFamiliar;
    public int numeroDeMoradores;
    public double gastoComLuz;
    public double gastoComAgua;
    public double gastoComInternet;
    public double valorMensalidadeDaAcademia;

    public double calcularTotalDeDespesas(){
        double totalDeDespesas;

        totalDeDespesas = gastoComAgua + gastoComInternet + gastoComLuz + (valorMensalidadeDaAcademia * numeroDeMoradores);

        return totalDeDespesas;
    }

    public double calcularRendaFamiliarLiquida(){
        double rendaFamiliarLiquida;

        rendaFamiliarLiquida = rendaFamiliar - calcularTotalDeDespesas();

        return rendaFamiliarLiquida;
    }

}
