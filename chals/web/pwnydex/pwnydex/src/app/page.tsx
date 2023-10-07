"use client";
import { FormEvent, useEffect, useState } from 'react';

function PwnydexEntry(pwnymon: Pwnymon) {
  const { id, name, description, image } = pwnymon;
  return (
    <div className="flex flex-row bg-[#222222] border-2 border-[#333333] rounded-xl">
      <div className="flex flex-col p-4">
        <p className="text-2xl">
          #{id} - {name}
        </p>
        <img src={image} alt={name} className="w-32 h-32 self-center" />
        <p className="text-sm">{description}</p>
      </div>
    </div>
  );
}

export default function Page() {
  const [pwnymons, setPwnymons] = useState<Pwnymon[]>([]);

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const search = formData.get('q') as string;
    const response = await fetch(`/search?q=${search}`);
    const data = await response.json();
    setPwnymons(data);
  }

  useEffect(() => {
    (async () => {
      const response = await fetch(`/search?q=`);
      const data = await response.json();
      setPwnymons(data);
    })();
  }, []);

  return (
    <div className="flex flex-col container mt-8 p-4 gap-4">
      <h1 className="text-4xl font-bold">
        Pwnydex
      </h1>
      <p>
        At this time, only the first generation of Pwnymon are available. The next generation is only available to invited trainers.
      </p>
      <div className="flex flex-row gap-4">
        <form onSubmit={onSubmit} className="flex w-full gap-4">
          <input
            name="q"
            type="text"
            className="flex-grow rounded-lg bg-[#222222] border-2 border-[#333333] px-4 py-2"
            placeholder="Search Pwnymon by name"
          />
          <button className="bg-[#333333] rounded-lg px-4 py-2">
            Search
          </button>
        </form>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
        {pwnymons.map((pwny) => (
          <PwnydexEntry key={pwny.id} {...pwny} />
        ))}
      </div>
    </div>
  );
}
