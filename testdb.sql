--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.7
-- Dumped by pg_dump version 9.5.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: employees; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE employees (
    e_id integer NOT NULL,
    name character varying NOT NULL,
    m_id integer,
    date_of_join timestamp without time zone DEFAULT now(),
    value_in_company integer
);


ALTER TABLE employees OWNER TO root;

--
-- Name: employees_e_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE employees_e_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE employees_e_id_seq OWNER TO root;

--
-- Name: employees_e_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE employees_e_id_seq OWNED BY employees.e_id;


--
-- Name: employees_json; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE employees_json (
    e_id integer NOT NULL,
    subtree json,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now()
);


ALTER TABLE employees_json OWNER TO root;

--
-- Name: employees_json_e_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE employees_json_e_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE employees_json_e_id_seq OWNER TO root;

--
-- Name: employees_json_e_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE employees_json_e_id_seq OWNED BY employees_json.e_id;


--
-- Name: e_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY employees ALTER COLUMN e_id SET DEFAULT nextval('employees_e_id_seq'::regclass);


--
-- Name: e_id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY employees_json ALTER COLUMN e_id SET DEFAULT nextval('employees_json_e_id_seq'::regclass);


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: root
--

COPY employees (e_id, name, m_id, date_of_join, value_in_company) FROM stdin;
2	Suresh	1	2017-07-15 22:52:40.647731	28
3	Pappan	1	2017-07-15 22:52:59.586479	27
4	Tim	1	2017-07-15 22:53:45.758659	27
5	Berners	1	2017-07-15 22:53:54.655714	26
6	Lee	2	2017-07-15 23:00:37.496253	20
7	Michael	2	2017-07-15 23:00:42.32381	19
8	Jordan	2	2017-07-15 23:01:55.665889	20
9	Mahatama	2	2017-07-15 23:02:01.72498	18
10	Gandhi	3	2017-07-15 23:02:48.896084	15
11	Elon	3	2017-07-15 23:02:59.100911	15
12	Musk	3	2017-07-15 23:03:02.733885	13
13	Dan	3	2017-07-15 23:03:07.229943	14
14	Bilzerian	4	2017-07-15 23:03:12.847072	10
15	Susan	4	2017-07-15 23:03:16.25593	11
16	Aman	7	2017-07-15 23:03:19.448908	6
17	Aryan	7	2017-07-15 23:03:22.46368	8
18	Pandey	8	2017-07-15 23:03:25.456856	5
19	Dubey	8	2017-07-15 23:03:29.513587	3
20	Pavlos	8	2017-07-15 23:03:32.984175	2
1	Ramesh	0	2017-07-15 22:52:02.861632	30
\.


--
-- Name: employees_e_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('employees_e_id_seq', 1, false);


--
-- Data for Name: employees_json; Type: TABLE DATA; Schema: public; Owner: root
--

COPY employees_json (e_id, subtree, created_at, updated_at) FROM stdin;
\.


--
-- Name: employees_json_e_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('employees_json_e_id_seq', 1, false);


--
-- Name: employees_json_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY employees_json
    ADD CONSTRAINT employees_json_pkey PRIMARY KEY (e_id);


--
-- Name: employees_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (e_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

