import { useQuery } from "@tanstack/react-query";

import categoriaService from "../services/categoriaService";

export function useCategorias() {
  return useQuery({
    queryKey: ["categorias"],
    queryFn: categoriaService.listar,
    staleTime: 1000 * 60 * 60,
  });
}