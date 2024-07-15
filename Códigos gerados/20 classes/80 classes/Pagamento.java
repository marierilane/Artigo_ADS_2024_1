package Diagrama de Classes Refatorado;

import java.util.Collection;

public interface Pagamento {

	private int id;

	private string status;

	private date data;

	private NFe nFe;

	private Collection<Pedido> pedido;

	private Controlador2 controlador2;

	/**
	 *  
	 */
	public abstract void selecionarTipoPagamaento();

	/**
	 *  
	 */
	public abstract void revisaoFraude();

	/**
	 *  
	 */
	public abstract void validarPagamento();

	/**
	 *  
	 */
	protected abstract double calcularPreco();

	/**
	 *  
	 */
	protected abstract void gerarDesconto();

}
