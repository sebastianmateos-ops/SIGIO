import { useQuery } from "@tanstack/react-query";

import implementoService from "../services/implementoService";

export function useImplementos() {
  return useQuery({
    queryKey: ["implementos"],

    queryFn: () =>
      implementoService.listar(),
  });
}