import axios from 'axios';
import { API_HOST } from '../consts';


export const makeFinancialProposal = (data) =>
  axios.post(`${API_HOST}/financial/financial-proposal/make_proposal`, { ...data })
    .then(res => res.data)
    .catch(err => console.error(err))

export const fetchPersons = () =>
  axios.get()
    .then()
    .catch()

export const fetchFields = () =>
  axios.get()
    .then()
    .catch()