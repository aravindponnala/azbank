import { useEffect, useState } from "react"
import { getAccounts, depositToAccount } from "../api"

export default function AccountList({ onSelect }) {
  const [accounts, setAccounts] = useState([])

useEffect(() => {
  getAccounts()
    .then(res => {
      console.log("Accounts API response:", res.data)
      setAccounts(res.data)
    })
    .catch(err => console.error("Error fetching accounts:", err))
}, [])

  const handleDeposit = async (id) => {
    await depositToAccount(id, 1000)
    alert("Deposited $10")
    console.log('JJJJJJJJJKKKKKKKMMMMMMMMMMMM')
    const res = await getAccounts()
    console.log(res,'----')
    setAccounts(res.data)
  }

  return (
    <div style={{ marginBottom: 20 }}>
      <h3>Accounts (from Django -----)</h3>
      {accounts.map(a => (
        <div key={a.id} style={{ padding: 8, border: "1px solid #ddd", marginBottom: 5 }}>
          <p><strong>{a.number}</strong> — Balance: {(a.balance_cents / 100).toFixed(2)} {a.currency}</p>
          <button onClick={() => handleDeposit(a.id)}>Deposit $10</button>
          <button onClick={() => onSelect(a.number)} style={{ marginLeft: 10 }}>View Transactions</button>
        </div>
      ))}
    </div>
  )
}
