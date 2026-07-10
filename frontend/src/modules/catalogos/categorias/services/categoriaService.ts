import api from "@/api/axios";
import type { Categoria } from "../types/categoria";

class CategoriaService {
  async listar(): Promise<Categoria[]> {
    const response = await api.get<Categoria[]>(
      "/categorias",
    );

    return response.data;
  }
}

export default new CategoriaService();