"use client";
import { useEffect, useState } from "react";

type Mutation = {
  position: number;
  probability: number;
};

const EvoResult = ({ gene }: { gene: string }) => {
  const [mutations, setMutations] = useState<Mutation[]>([]);
  const [hasUpdated, setHasUpdated] = useState(false);

  useEffect(() => {
    const fetchEvoResults = async () => {
      const res = await fetch(`/api/evo?gene=${gene}`);
      const data = await res.json();
      setMutations(data.mutations);
    };
    setHasUpdated(true);

    fetchEvoResults();
  }, []);
  return (
    <div className="flex flex-col gap-4">
      {(hasUpdated) ? mutations.map((mutation, index) => (
        <div
          key={index}
          className="hover-container bg-[#16113a] p-2"
        >
          <p>Position: {mutation.position}</p>
          <p>Probability: {mutation.probability}</p>
        </div>
      )): <p>Loading...</p>}
    </div>
  );
};

export default EvoResult;
