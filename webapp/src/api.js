import axios from 'axios'

// The base API URL (in Docker: accounts = http://localhost:8001, payments = http://localhost:8002)
const DJANGO_API = import.meta.env.VITE_DJANGO_API || 'http://localhost:8001/api'
const FASTAPI_API = import.meta.env.VITE_FASTAPI_API || 'http://localhost:8002'

// Django APIs
export const getAccounts = async () => axios.get(`${DJANGO_API}/accounts/`)
export const createAccount = async (payload) => axios.post(`${DJANGO_API}/accounts/`, payload)
export const depositToAccount = async (id, amount_cents) =>
  axios.post(`${DJANGO_API}/accounts/${id}/deposit/`, { amount_cents })

// FastAPI APIs
export const createTransaction = async (payload) =>
  axios.post(`${FASTAPI_API}/transactions/`, payload)

export const queryGraphQL = async (account_number) => {
  const query = `
    query($account_number: String!) {
      transactions(account_number: $account_number) {
        id
        amount_cents
        memo
      }
    }
  `
  const { data } = await axios.post(`${FASTAPI_API}/graphql`, { query, variables: { account_number } })
  return data
}
