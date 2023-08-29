import axios from 'axios';
import { API_HOST } from '../consts';

export const fetchFinancialProposal = () =>
  axios.get(`${API_HOST}/financial/financial-proposal`)
    .then(res => res.data)
    .catch(err => console.error(err))

export const createFinancialProposal = (data) =>
  axios.post(`${API_HOST}/financial/financial-proposal/make_proposal`, { ...data })
    .then(res => res.data)
    .catch(err => console.error(err))

export const fetchFields = () =>
  axios.get(`${API_HOST}/financial/proposal-fields`)
    .then(res => res.data)
    .catch(err => console.error(err))

export const fetchPersons = () =>
  axios.get(`${API_HOST}/personal/persons`)
    .then(res => res.data)
    .catch(err => console.error(err))