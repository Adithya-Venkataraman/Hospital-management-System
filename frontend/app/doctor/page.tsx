"use client";

import React, { useEffect, useState } from "react";

export default function DoctorPage() {
  const [patients, setPatients] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/doctor/1")
      .then((res) => res.json())
      .then((data) => setPatients(data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Doctor Dashboard</h2>

      {patients.map((p) => (
        <p key={p.patient_id}>{p.patient_name}</p>
      ))}
    </div>
  );
}
