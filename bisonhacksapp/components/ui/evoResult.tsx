"use client";
import { useEffect, useState } from "react";

const EvoResult = ({ gene }: { gene: string }) => {
  const [mutations, setMutations] = useState("");

  useEffect(() => {
    const fetchEvoResults = async () => {
      const res = await fetch(`/api/evo?gene=${gene}`);
      const data = await res.json();
      setMutations(data.mutations);
    };

    fetchEvoResults();
  }, []);
  return (
    <p>{mutations}</p>
  );
};

export default EvoResult;
