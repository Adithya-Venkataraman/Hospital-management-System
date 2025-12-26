"use client";

import React, { useEffect, useState } from "react";

export default function Page() {
  const [doctors, setDoctors] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/doctors")
      .then((res) => res.json())
      .then((data) => setDoctors(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Admin Dashboard</h1>

      <h3>Doctors</h3>
      {doctors.length === 0 && <p>Loading...</p>}

      {doctors.map((doc) => (
        <p key={doc.doctor_id}>{doc.doctor_name}</p>
      ))}
    </div>
  );
}
