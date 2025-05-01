--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Debian 14.5-2.pgdg110+2)
-- Dumped by pg_dump version 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: demo_pets_user
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO demo_pets_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: nutrition_plan; Type: TABLE; Schema: public; Owner: demo_pets_user
--

CREATE TABLE public.nutrition_plan (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL,
    meal json NOT NULL,
    starting_date timestamp without time zone NOT NULL
);


ALTER TABLE public.nutrition_plan OWNER TO demo_pets_user;

--
-- Name: nutrition_plan_id_seq; Type: SEQUENCE; Schema: public; Owner: demo_pets_user
--

CREATE SEQUENCE public.nutrition_plan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.nutrition_plan_id_seq OWNER TO demo_pets_user;

--
-- Name: nutrition_plan_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: demo_pets_user
--

ALTER SEQUENCE public.nutrition_plan_id_seq OWNED BY public.nutrition_plan.id;


--
-- Name: pet; Type: TABLE; Schema: public; Owner: demo_pets_user
--

CREATE TABLE public.pet (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    owner_id integer,
    nutrition_plan_id integer
);


ALTER TABLE public.pet OWNER TO demo_pets_user;

--
-- Name: pet_id_seq; Type: SEQUENCE; Schema: public; Owner: demo_pets_user
--

CREATE SEQUENCE public.pet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pet_id_seq OWNER TO demo_pets_user;

--
-- Name: pet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: demo_pets_user
--

ALTER SEQUENCE public.pet_id_seq OWNED BY public.pet.id;


--
-- Name: pet_owner; Type: TABLE; Schema: public; Owner: demo_pets_user
--

CREATE TABLE public.pet_owner (
    id integer NOT NULL,
    name character varying NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL,
    home_address character varying NOT NULL
);


ALTER TABLE public.pet_owner OWNER TO demo_pets_user;

--
-- Name: pet_owner_id_seq; Type: SEQUENCE; Schema: public; Owner: demo_pets_user
--

CREATE SEQUENCE public.pet_owner_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pet_owner_id_seq OWNER TO demo_pets_user;

--
-- Name: pet_owner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: demo_pets_user
--

ALTER SEQUENCE public.pet_owner_id_seq OWNED BY public.pet_owner.id;


--
-- Name: pet_trainer_association; Type: TABLE; Schema: public; Owner: demo_pets_user
--

CREATE TABLE public.pet_trainer_association (
    pet_id integer NOT NULL,
    trainer_id character varying NOT NULL
);


ALTER TABLE public.pet_trainer_association OWNER TO demo_pets_user;

--
-- Name: trainer; Type: TABLE; Schema: public; Owner: demo_pets_user
--

CREATE TABLE public.trainer (
    trainer_id character varying NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL,
    phone_no character varying NOT NULL,
    email character varying NOT NULL,
    date_started timestamp without time zone NOT NULL
);


ALTER TABLE public.trainer OWNER TO demo_pets_user;

--
-- Name: nutrition_plan id; Type: DEFAULT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.nutrition_plan ALTER COLUMN id SET DEFAULT nextval('public.nutrition_plan_id_seq'::regclass);


--
-- Name: pet id; Type: DEFAULT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet ALTER COLUMN id SET DEFAULT nextval('public.pet_id_seq'::regclass);


--
-- Name: pet_owner id; Type: DEFAULT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet_owner ALTER COLUMN id SET DEFAULT nextval('public.pet_owner_id_seq'::regclass);


--
-- Data for Name: nutrition_plan; Type: TABLE DATA; Schema: public; Owner: demo_pets_user
--

COPY public.nutrition_plan (id, name, description, meal, starting_date) FROM stdin;
1	Pickles Meal Deal	High vitamin meal with low carbs	{"protein": "Chicken", "carb": "Brown Rice", "fibre": "Broccolli"}	2023-10-10 00:00:00
2	Rosie Roast Plan	High protein for the aspiring competitor	{"protein": "Beef", "carb": "Dog Pasta", "fibre": "Beans"}	2023-08-23 00:00:00
3	Cooper Carb Load	Dense carb plan for a picky eater	{"protein": "Fish", "carb": "Puppy Penne", "fibre": "Corn"}	2021-03-03 00:00:00
\.


--
-- Data for Name: pet; Type: TABLE DATA; Schema: public; Owner: demo_pets_user
--

COPY public.pet (id, name, age, owner_id, nutrition_plan_id) FROM stdin;
3	Abbie	4	1	\N
1	Pickles	2	1	1
2	Rosie	1	1	2
4	Cooper	3	2	3
\.


--
-- Data for Name: pet_owner; Type: TABLE DATA; Schema: public; Owner: demo_pets_user
--

COPY public.pet_owner (id, name, email, password, home_address) FROM stdin;
1	Alice	alice@bigpond.com	iLovePuppies123!thisisahash	Unit 1, 124 Copernicus Avenue
2	Bob	bob@ymail.com	pattingGiver381thisisahash	912 Dylan Lane
\.


--
-- Data for Name: pet_trainer_association; Type: TABLE DATA; Schema: public; Owner: demo_pets_user
--

COPY public.pet_trainer_association (pet_id, trainer_id) FROM stdin;
1	TR-013
2	TR-013
3	TR-047
4	TR-013
\.


--
-- Data for Name: trainer; Type: TABLE DATA; Schema: public; Owner: demo_pets_user
--

COPY public.trainer (trainer_id, name, description, phone_no, email, date_started) FROM stdin;
TR-013	Eddie Bark	Export in pet cardio	04442123123	eddie.bark@plusWoofers.com	2021-01-07 00:00:00
TR-047	Lara Meowstein	Professional pet bodybuilding coach	0333789789	lara.meowstein@plusWoofers.com	2019-12-31 00:00:00
\.


--
-- Name: nutrition_plan_id_seq; Type: SEQUENCE SET; Schema: public; Owner: demo_pets_user
--

SELECT pg_catalog.setval('public.nutrition_plan_id_seq', 3, true);


--
-- Name: pet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: demo_pets_user
--

SELECT pg_catalog.setval('public.pet_id_seq', 4, true);


--
-- Name: pet_owner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: demo_pets_user
--

SELECT pg_catalog.setval('public.pet_owner_id_seq', 2, true);


--
-- Name: nutrition_plan nutrition_plan_name_key; Type: CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.nutrition_plan
    ADD CONSTRAINT nutrition_plan_name_key UNIQUE (name);


--
-- Name: nutrition_plan nutrition_plan_pkey; Type: CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.nutrition_plan
    ADD CONSTRAINT nutrition_plan_pkey PRIMARY KEY (id);


--
-- Name: pet pet_name_key; Type: CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_name_key UNIQUE (name);


--
-- Name: pet_owner pet_owner_name_key; Type: CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet_owner
    ADD CONSTRAINT pet_owner_name_key UNIQUE (name);


--
-- Name: pet_owner pet_owner_pkey; Type: CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet_owner
    ADD CONSTRAINT pet_owner_pkey PRIMARY KEY (id);


--
-- Name: pet pet_pkey; Type: CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_pkey PRIMARY KEY (id);


--
-- Name: pet_trainer_association pet_trainer_association_pkey; Type: CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet_trainer_association
    ADD CONSTRAINT pet_trainer_association_pkey PRIMARY KEY (pet_id, trainer_id);


--
-- Name: trainer trainer_pkey; Type: CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.trainer
    ADD CONSTRAINT trainer_pkey PRIMARY KEY (trainer_id);


--
-- Name: ix_nutrition_plan_id; Type: INDEX; Schema: public; Owner: demo_pets_user
--

CREATE INDEX ix_nutrition_plan_id ON public.nutrition_plan USING btree (id);


--
-- Name: ix_pet_id; Type: INDEX; Schema: public; Owner: demo_pets_user
--

CREATE INDEX ix_pet_id ON public.pet USING btree (id);


--
-- Name: ix_pet_owner_id; Type: INDEX; Schema: public; Owner: demo_pets_user
--

CREATE INDEX ix_pet_owner_id ON public.pet_owner USING btree (id);


--
-- Name: ix_trainer_trainer_id; Type: INDEX; Schema: public; Owner: demo_pets_user
--

CREATE INDEX ix_trainer_trainer_id ON public.trainer USING btree (trainer_id);


--
-- Name: pet pet_nutrition_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_nutrition_plan_id_fkey FOREIGN KEY (nutrition_plan_id) REFERENCES public.nutrition_plan(id);


--
-- Name: pet pet_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet
    ADD CONSTRAINT pet_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES public.pet_owner(id);


--
-- Name: pet_trainer_association pet_trainer_association_pet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet_trainer_association
    ADD CONSTRAINT pet_trainer_association_pet_id_fkey FOREIGN KEY (pet_id) REFERENCES public.pet(id);


--
-- Name: pet_trainer_association pet_trainer_association_trainer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: demo_pets_user
--

ALTER TABLE ONLY public.pet_trainer_association
    ADD CONSTRAINT pet_trainer_association_trainer_id_fkey FOREIGN KEY (trainer_id) REFERENCES public.trainer(trainer_id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: demo_pets_user
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

