PGDMP                         y            world_chase_tag_db    13.2 (Debian 13.2-1.pgdg100+1)    13.2 (Debian 13.2-1.pgdg100+1) I    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16385    world_chase_tag_db    DATABASE     f   CREATE DATABASE world_chase_tag_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';
 "   DROP DATABASE world_chase_tag_db;
                adempus    false            �            1259    17668    athlete    TABLE       CREATE TABLE public.athlete (
    id integer NOT NULL,
    team bigint NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    birth_date date NOT NULL,
    image_url text,
    sm_handle character varying(50)
);
    DROP TABLE public.athlete;
       public         heap    adempus    false            �            1259    17666    athlete_id_seq    SEQUENCE     �   CREATE SEQUENCE public.athlete_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.athlete_id_seq;
       public          adempus    false    207            �           0    0    athlete_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.athlete_id_seq OWNED BY public.athlete.id;
          public          adempus    false    206            �            1259    17791    chase    TABLE     
  CREATE TABLE public.chase (
    id integer NOT NULL,
    match bigint NOT NULL,
    chase_no integer NOT NULL,
    chaser bigint NOT NULL,
    evader bigint NOT NULL,
    tag_made boolean NOT NULL,
    tag_time double precision,
    sudden_death boolean NOT NULL
);
    DROP TABLE public.chase;
       public         heap    adempus    false            �            1259    17789    chase_id_seq    SEQUENCE     �   CREATE SEQUENCE public.chase_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.chase_id_seq;
       public          adempus    false    211            �           0    0    chase_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.chase_id_seq OWNED BY public.chase.id;
          public          adempus    false    210            �            1259    17613    country    TABLE     m   CREATE TABLE public.country (
    id integer NOT NULL,
    name text NOT NULL,
    flag_url text NOT NULL
);
    DROP TABLE public.country;
       public         heap    adempus    false            �            1259    17611    country_id_seq    SEQUENCE     �   CREATE SEQUENCE public.country_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.country_id_seq;
       public          adempus    false    201            �           0    0    country_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.country_id_seq OWNED BY public.country.id;
          public          adempus    false    200            �            1259    17628    group    TABLE     Q   CREATE TABLE public."group" (
    id integer NOT NULL,
    name text NOT NULL
);
    DROP TABLE public."group";
       public         heap    adempus    false            �            1259    17626    group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.group_id_seq;
       public          adempus    false    203            �           0    0    group_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.group_id_seq OWNED BY public."group".id;
          public          adempus    false    202            �            1259    17751    match    TABLE     0  CREATE TABLE public.match (
    id integer NOT NULL,
    team_a bigint NOT NULL,
    team_b bigint NOT NULL,
    winning_team bigint NOT NULL,
    loosing_team bigint NOT NULL,
    team_a_points integer NOT NULL,
    team_b_points integer NOT NULL,
    date date NOT NULL,
    video_url text NOT NULL
);
    DROP TABLE public.match;
       public         heap    adempus    false            �            1259    17749    match_id_seq    SEQUENCE     �   CREATE SEQUENCE public.match_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.match_id_seq;
       public          adempus    false    209            �           0    0    match_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.match_id_seq OWNED BY public.match.id;
          public          adempus    false    208            �            1259    17641    team    TABLE     �   CREATE TABLE public.team (
    id integer NOT NULL,
    name character varying(75) NOT NULL,
    "group" integer,
    logo_url text,
    country smallint NOT NULL
);
    DROP TABLE public.team;
       public         heap    adempus    false            �            1259    17639    team_id_seq    SEQUENCE     �   CREATE SEQUENCE public.team_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.team_id_seq;
       public          adempus    false    205            �           0    0    team_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE public.team_id_seq OWNED BY public.team.id;
          public          adempus    false    204                       2604    17671 
   athlete id    DEFAULT     h   ALTER TABLE ONLY public.athlete ALTER COLUMN id SET DEFAULT nextval('public.athlete_id_seq'::regclass);
 9   ALTER TABLE public.athlete ALTER COLUMN id DROP DEFAULT;
       public          adempus    false    207    206    207                       2604    17794    chase id    DEFAULT     d   ALTER TABLE ONLY public.chase ALTER COLUMN id SET DEFAULT nextval('public.chase_id_seq'::regclass);
 7   ALTER TABLE public.chase ALTER COLUMN id DROP DEFAULT;
       public          adempus    false    210    211    211                       2604    17616 
   country id    DEFAULT     h   ALTER TABLE ONLY public.country ALTER COLUMN id SET DEFAULT nextval('public.country_id_seq'::regclass);
 9   ALTER TABLE public.country ALTER COLUMN id DROP DEFAULT;
       public          adempus    false    201    200    201                       2604    17631    group id    DEFAULT     f   ALTER TABLE ONLY public."group" ALTER COLUMN id SET DEFAULT nextval('public.group_id_seq'::regclass);
 9   ALTER TABLE public."group" ALTER COLUMN id DROP DEFAULT;
       public          adempus    false    202    203    203                       2604    17754    match id    DEFAULT     d   ALTER TABLE ONLY public.match ALTER COLUMN id SET DEFAULT nextval('public.match_id_seq'::regclass);
 7   ALTER TABLE public.match ALTER COLUMN id DROP DEFAULT;
       public          adempus    false    209    208    209                       2604    17644    team id    DEFAULT     b   ALTER TABLE ONLY public.team ALTER COLUMN id SET DEFAULT nextval('public.team_id_seq'::regclass);
 6   ALTER TABLE public.team ALTER COLUMN id DROP DEFAULT;
       public          adempus    false    204    205    205            �          0    17668    athlete 
   TABLE DATA           d   COPY public.athlete (id, team, first_name, last_name, birth_date, image_url, sm_handle) FROM stdin;
    public          adempus    false    207   =Q       �          0    17791    chase 
   TABLE DATA           f   COPY public.chase (id, match, chase_no, chaser, evader, tag_made, tag_time, sudden_death) FROM stdin;
    public          adempus    false    211   �V       �          0    17613    country 
   TABLE DATA           5   COPY public.country (id, name, flag_url) FROM stdin;
    public          adempus    false    201   Z       �          0    17628    group 
   TABLE DATA           +   COPY public."group" (id, name) FROM stdin;
    public          adempus    false    203   "f       �          0    17751    match 
   TABLE DATA           ~   COPY public.match (id, team_a, team_b, winning_team, loosing_team, team_a_points, team_b_points, date, video_url) FROM stdin;
    public          adempus    false    209   Of       �          0    17641    team 
   TABLE DATA           D   COPY public.team (id, name, "group", logo_url, country) FROM stdin;
    public          adempus    false    205   1g       �           0    0    athlete_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.athlete_id_seq', 74, true);
          public          adempus    false    206            �           0    0    chase_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.chase_id_seq', 1370, true);
          public          adempus    false    210            �           0    0    country_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.country_id_seq', 258, true);
          public          adempus    false    200            �           0    0    group_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.group_id_seq', 4, true);
          public          adempus    false    202            �           0    0    match_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.match_id_seq', 128, true);
          public          adempus    false    208            �           0    0    team_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.team_id_seq', 28, true);
          public          adempus    false    204            /           2606    17678    athlete athlete_image_url_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.athlete
    ADD CONSTRAINT athlete_image_url_key UNIQUE (image_url);
 G   ALTER TABLE ONLY public.athlete DROP CONSTRAINT athlete_image_url_key;
       public            adempus    false    207            1           2606    17676    athlete athlete_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.athlete
    ADD CONSTRAINT athlete_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.athlete DROP CONSTRAINT athlete_pkey;
       public            adempus    false    207            3           2606    17680    athlete athlete_sm_handle_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.athlete
    ADD CONSTRAINT athlete_sm_handle_key UNIQUE (sm_handle);
 G   ALTER TABLE ONLY public.athlete DROP CONSTRAINT athlete_sm_handle_key;
       public            adempus    false    207            <           2606    17796    chase chase_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.chase
    ADD CONSTRAINT chase_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.chase DROP CONSTRAINT chase_pkey;
       public            adempus    false    211                       2606    17625    country country_flag_url_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_flag_url_key UNIQUE (flag_url);
 F   ALTER TABLE ONLY public.country DROP CONSTRAINT country_flag_url_key;
       public            adempus    false    201                       2606    17623    country country_name_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_name_key UNIQUE (name);
 B   ALTER TABLE ONLY public.country DROP CONSTRAINT country_name_key;
       public            adempus    false    201            !           2606    17621    country country_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.country DROP CONSTRAINT country_pkey;
       public            adempus    false    201            #           2606    17638    group group_name_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public."group"
    ADD CONSTRAINT group_name_key UNIQUE (name);
 @   ALTER TABLE ONLY public."group" DROP CONSTRAINT group_name_key;
       public            adempus    false    203            %           2606    17636    group group_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public."group"
    ADD CONSTRAINT group_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public."group" DROP CONSTRAINT group_pkey;
       public            adempus    false    203            :           2606    17759    match match_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.match
    ADD CONSTRAINT match_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.match DROP CONSTRAINT match_pkey;
       public            adempus    false    209            )           2606    17653    team team_logo_url_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_logo_url_key UNIQUE (logo_url);
 @   ALTER TABLE ONLY public.team DROP CONSTRAINT team_logo_url_key;
       public            adempus    false    205            +           2606    17651    team team_name_key 
   CONSTRAINT     M   ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_name_key UNIQUE (name);
 <   ALTER TABLE ONLY public.team DROP CONSTRAINT team_name_key;
       public            adempus    false    205            -           2606    17649    team team_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.team DROP CONSTRAINT team_pkey;
       public            adempus    false    205            4           1259    17681    idx_athlete__team    INDEX     E   CREATE INDEX idx_athlete__team ON public.athlete USING btree (team);
 %   DROP INDEX public.idx_athlete__team;
       public            adempus    false    207            =           1259    17797    idx_chase__chaser    INDEX     E   CREATE INDEX idx_chase__chaser ON public.chase USING btree (chaser);
 %   DROP INDEX public.idx_chase__chaser;
       public            adempus    false    211            >           1259    17798    idx_chase__evader    INDEX     E   CREATE INDEX idx_chase__evader ON public.chase USING btree (evader);
 %   DROP INDEX public.idx_chase__evader;
       public            adempus    false    211            ?           1259    17799    idx_chase__match    INDEX     C   CREATE INDEX idx_chase__match ON public.chase USING btree (match);
 $   DROP INDEX public.idx_chase__match;
       public            adempus    false    211            5           1259    17760    idx_match__loosing_team    INDEX     Q   CREATE INDEX idx_match__loosing_team ON public.match USING btree (loosing_team);
 +   DROP INDEX public.idx_match__loosing_team;
       public            adempus    false    209            6           1259    17761    idx_match__team_a    INDEX     E   CREATE INDEX idx_match__team_a ON public.match USING btree (team_a);
 %   DROP INDEX public.idx_match__team_a;
       public            adempus    false    209            7           1259    17762    idx_match__team_b    INDEX     E   CREATE INDEX idx_match__team_b ON public.match USING btree (team_b);
 %   DROP INDEX public.idx_match__team_b;
       public            adempus    false    209            8           1259    17763    idx_match__winning_team    INDEX     Q   CREATE INDEX idx_match__winning_team ON public.match USING btree (winning_team);
 +   DROP INDEX public.idx_match__winning_team;
       public            adempus    false    209            &           1259    17654    idx_team__country    INDEX     E   CREATE INDEX idx_team__country ON public.team USING btree (country);
 %   DROP INDEX public.idx_team__country;
       public            adempus    false    205            '           1259    17655    idx_team__group    INDEX     C   CREATE INDEX idx_team__group ON public.team USING btree ("group");
 #   DROP INDEX public.idx_team__group;
       public            adempus    false    205            B           2606    17682    athlete fk_athlete__team    FK CONSTRAINT     �   ALTER TABLE ONLY public.athlete
    ADD CONSTRAINT fk_athlete__team FOREIGN KEY (team) REFERENCES public.team(id) ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.athlete DROP CONSTRAINT fk_athlete__team;
       public          adempus    false    205    2861    207            G           2606    17800    chase fk_chase__chaser    FK CONSTRAINT     �   ALTER TABLE ONLY public.chase
    ADD CONSTRAINT fk_chase__chaser FOREIGN KEY (chaser) REFERENCES public.athlete(id) ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.chase DROP CONSTRAINT fk_chase__chaser;
       public          adempus    false    207    2865    211            H           2606    17805    chase fk_chase__evader    FK CONSTRAINT     �   ALTER TABLE ONLY public.chase
    ADD CONSTRAINT fk_chase__evader FOREIGN KEY (evader) REFERENCES public.athlete(id) ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.chase DROP CONSTRAINT fk_chase__evader;
       public          adempus    false    2865    211    207            I           2606    17810    chase fk_chase__match    FK CONSTRAINT     �   ALTER TABLE ONLY public.chase
    ADD CONSTRAINT fk_chase__match FOREIGN KEY (match) REFERENCES public.match(id) ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.chase DROP CONSTRAINT fk_chase__match;
       public          adempus    false    2874    211    209            C           2606    17764    match fk_match__loosing_team    FK CONSTRAINT     �   ALTER TABLE ONLY public.match
    ADD CONSTRAINT fk_match__loosing_team FOREIGN KEY (loosing_team) REFERENCES public.team(id) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.match DROP CONSTRAINT fk_match__loosing_team;
       public          adempus    false    2861    205    209            D           2606    17769    match fk_match__team_a    FK CONSTRAINT     �   ALTER TABLE ONLY public.match
    ADD CONSTRAINT fk_match__team_a FOREIGN KEY (team_a) REFERENCES public.team(id) ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.match DROP CONSTRAINT fk_match__team_a;
       public          adempus    false    209    2861    205            E           2606    17774    match fk_match__team_b    FK CONSTRAINT     �   ALTER TABLE ONLY public.match
    ADD CONSTRAINT fk_match__team_b FOREIGN KEY (team_b) REFERENCES public.team(id) ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.match DROP CONSTRAINT fk_match__team_b;
       public          adempus    false    209    205    2861            F           2606    17779    match fk_match__winning_team    FK CONSTRAINT     �   ALTER TABLE ONLY public.match
    ADD CONSTRAINT fk_match__winning_team FOREIGN KEY (winning_team) REFERENCES public.team(id) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.match DROP CONSTRAINT fk_match__winning_team;
       public          adempus    false    209    205    2861            @           2606    17656    team fk_team__country    FK CONSTRAINT     �   ALTER TABLE ONLY public.team
    ADD CONSTRAINT fk_team__country FOREIGN KEY (country) REFERENCES public.country(id) ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.team DROP CONSTRAINT fk_team__country;
       public          adempus    false    201    205    2849            A           2606    17661    team fk_team__group    FK CONSTRAINT     �   ALTER TABLE ONLY public.team
    ADD CONSTRAINT fk_team__group FOREIGN KEY ("group") REFERENCES public."group"(id) ON DELETE SET NULL;
 =   ALTER TABLE ONLY public.team DROP CONSTRAINT fk_team__group;
       public          adempus    false    203    205    2853            �   Y  x�}��r�6���St�U4�E�*;�3J�x�L<m��@(B �P�.�}��N�$�lw!����~�!�)K2�Y<Y�V�9�t��oƓ7�}��~h	U���g$]ʪb��9�����~�$�Iy�Ԟ���h���a��8y~�Xg�3|B⏢��Q��FBT��)i/�l[�E�R�jׄ�'B|ޫJ��M��O�N���U޼����U�o�0la6���#���v$^(Oư�k��fwb0�[ZU�V#�K�ē�j˚]v�Q��Gn5�G�}��')��Ұ�����H+�����I�������RkYKw�n�vt��$��~�p%���耚@H�����!��:��ЁO��]hY�{����N��V%Of$�F�p�!�5�l�2�m�xNjD��Z��.r����s<���F!�Ȧx����gZ�
F阌���F��=
*��jܽH���i���N<)�n�GF�i4v��6x���B98�h5�鴺=!�f$^�	��_��,�s�=��n�����JY���Rz/�;��3e�#Z��!����2��ET����<��O�ژ=i����(�k;��B�	��8����tNڷ�27��ā�� w�xzA�Ν�!3lLʕ*��z�������(� y���{���H�E��O-�=�)x��3"�v�>t��1 ��/f<Cvg8r�T�4q��s ��L˳���|�++[U(�(G��3������5B~k�&�6<����_�;��P��ٸ��;�g����a?w�d�0�7�D=/�a+��<S��g32����o[�D����s�����`�Z�p��^`! y>!�����V�{����)�?`j����Z�F'7<���R(��Fa��S���|NR$�PS��+���:�E���$��ſ����z�R@|2f��� g/��"gqs��h�'	��5u��V�3����F>`>I��ޮ�CY�:r��u�ᓌ����0��'J��9��{��°5�xcʮ��c�H�W�_7&d�hP���lDԹ��'H%f��l��̌�`�b�P�H��4�wB��x�Bc����ŃF�nq5�Ϝ�%��� ���4.CFE-�Z�La���4�����7�J��	�*BԂ�$8���]Y�e)����8�3>E�f�Jx����KI���<h)4���폕P��"9�m��	\k��]uZ��%l��)���^����""�ag�}����n�
7�3û�U �����o������� �Sdj�-b�a�x�(�oîk��Ƥ\�ZK6�Z��(J�`�YB��S�;�YݒX���y䳔�+�Mإ�u����: >�HV[ɝ�r_9�ov9��$\��M�Νv�܉z8�#��?5he�      �   O  x�UVK��0[+�ɘ��w��� ���;3�@, A?�j�<���W������2�NOp�������"*�Zb����n%��	'�~�Ax���q�1I���O��^b��j�L��A�]��o�jM�Dm���-��e7ɶ�=@�%4)��B�qv(i�
��K���:J>u�w�$�.�]��|v�����9~�F8�p�S��Lb ��.f����)m��I"Q��c^�M�A<.���h�t�֝�;�sTH6��a������L�
	����R�!�ͺt�)��L�ڦ����8?���\P��%��R�`��o��7���
�T@6�٘��#aF8�3�p�|��P�D���]�V�t��㾠(�m��L$`+ </��W��OI�`�尙���[�@�tG��z���ᦰg�d�K|
�W���]�1�u�}�\�����R���qù���[.����[i4)ؐ4ދ�_�Hށ���;LI�fl;ou͜��J9��I�v�C�������S�����1�h�TJ�9��Xp��)��cN:���d���~pA�7!��Ψw"�� �&oU� z�������������t���~��d�I�@_���q�od�O1���I�f�����=q\s1�̄DM�uN[d�>~��n{Uk��υ��p�l�o,y;��&��.=ǳ&�sF�� ����ȵ&�,C�ه��?���I�&{��-����9g�"�4_߃��R�Ğ��N��x,��%�R�������׍�*ҍ�w5]����3C}+��y�%�&���.�z���ʐf������{�^���ʎ�      �     x��ZMsܸ=ÿ��8U��~37Y�-Y�H����HB$4$A���g��%9���[���XD���B��bU�A�_��~����P+�9k��?���sǛ�~�T����͛�}�up�y\�Rs#&�by"bg�M�9>���0����<�C�㺜kb/��@4��:%T�κ^O����3��/�ܾOQoS���uedE�.��
������i�[��^hXmy����!;�'���09�(��p@��K�s������|]M��	��8]r�Be��3�NM�ƒ	�BD��T�J�ʙ�^+�&���
�M�k1�~ f���]#�ޏr��ٻYo`o�>)?��w�k8EO�:�`������u�ؾwj�G�����Z��aR�/3Vq�}���ޏwR	��{J���Jl���������-'�h��!he)@w´BөV:yE@����AN[Qh#�{N,�D�Lծ�i*:Լu��nHQf�q*�������3���CY6:y~��S�CN0V9�D;W�����V�?��tU���b��s��sb����Ԝ���U�1�e'+�c�Bv��9 �O���'���N���?�i(���뿍�?\m��"x���'�G��NXq�R���8h��[��	�����2��?�*'�8�KiS9MŖ�N�%!�ʉ*Q)���ը*'����@�E��G|�&>�e~�Z������O��Vü �<��ʵ��؏�N*��X8����ℒd�#�6>�+`�j~���/�T��W��֤`���s��\z�  �ˁ��vԧ��ߑN�Na�A5��}p��j����(�D���b2���K���f??Ɖ3M�/b2B�i��Ĭ)�>ӌ]hi� P.AӜ=�T�����0�T#���g+v1k5�Fc.!F�>[�r ����,ԋ?O�]�d�����NQ�.a����J�AL��<���XW+qzQ�-Y�>h>T~�>�Hg�^Qi\��A��R+��ԸY,Z�(F��)�˛|����8�� �n�5{��9�*�{�_xG���:�Fy�>jA6����<�"�tC��8����U���YR�@��`���3|�$�u�� ?-���T�����>&ŏsy��S�ߍ�\�
r�l6���b�����5�"L坚G6�B��:s���u����,X�˧�ݸl)��8E�K������l\Z��
pE��12?����g?ֵ�(��$�{��+v	#Rp�x���kv)�>֜�j�V�����u��q�о���N��A�׊"�-�U�.�$Zj��u���y �B��u����>Q"e����*'R ,gW���o'd��P����-a$��?l��nmMDdj�<?W�5=	���H�O��i������b�� bvU�=�vexG�	�[���T{�h�������^�1��'�kb�/�0��H�F<7Y�k1�������_�u�?�Y��v �KE�i�k	ΖY�����X�J'�}�䯥1�"�;���C�d`���
��6�(eX#O@1i��_�;����G�������f��-���oZ:�x|���������(�@�3���w1��+�ͮBh�n$X#�p���CJ#�J���bU,�Q
����a��>gR��;+`�Q��v&�C��a�n�o�x��>�O	WlC��t[D��g
�a�����U�����m�B!��oUW����=v p�p&M,����e�\������1��SE�Y=�
������;��k�{��[^���d=���[���K�},�-�=�S,/�e��S�Ċ.�F�2=�e����[{$:�ӟ�5̾��:��{8�[>C�$s�G��)0A[���գ|K��~J|�{�$�$zTN�pS�-�<z�x���"S0��⛤Tq<������`ԣS������8c���{IY�E��N�s�Yt��]p�w��|P�`�!��U�9uH4�"��-I�嘁ф�C�f&�X�����Y���B���O=*"�`���G�����_[�3�;I�6`�e��_�#w�����=�q���� ���s ��� 6?"����߫nOO�#�
6���3��0�#^����G��y�Ԃݿ���r���J�q�,ȏ�ٽ�B#�߲��d�؂�����R���F��y��g���g��j0b�䖶NLPO��2b�ˁ9(�sC�爵�X���?b�*,e�����!���)�bN{x�m&O�4�U�Փ�@�
�9��T1��"e�D��F����]���b��r�N�8?��	�+p:&7���|̾jEGnM"��q���t���NԂ@�(��G	}���='~'�Kщ��)8�*���EOzQ^P��|Z"0x��:�%o�'�]���]i�=�K>q;~�O��U����X}�8�Ҋ�7B���uTr7�~�Nx���,�xJHo»�5P	NMg�B��	�jbq��y1!�|��
�T����{������9�d�]t�#��ĴEhj�ʎ�0�Ql}C,������GP�.���d��qg��a��;����i��Ϲ����dhP\ኝ���j+\��u;۷|�1�u��k�?/ٓ"�Fj.��S�%٬�)���'��Am�	�u#��oPaʞd��7���Ee��f�s����0,��j#��� TF�Z�KN�E�fP�YsWA�Tɩ�c�G@�U���x�p��>x�(K�p ���\��ycD������٢��/R��Σ�?���eP:�y6�J�I��T��b�T���E�������g=��Č�����'rz���!���r�z.�>x{	�h�(��>l1�������%?�oܥ9on�N�1��� #���-��8�~0�E�F����b����ϳ�7�}���m�i�s�0s�O�팰�޷u�U����K���Z ���A�f�jR[��a!JB�W�-d�^�0���j��Nb��7-^��#Iد�E�U���Wٗ����|pe�o?�y��?�(      �      x�3�t�2�t�2�t�2�t����� ��      �   �   x����
�0�u�/i3�/+*(�*���Z���hԯ7�j�Uf��ÝF8\�b��e�y(��T�l[)eݏyIRKs[�Rd�k�G[.f*�x�2J���Z*x�����Քk�OV�4��R�1 >��y��Ի�S&C�����y�.y�DJh�7���C�#�%a�CM��W��s To7�����
:�lr����	�Gu�      �   _  x�M�QO�0��˯�{�m�,fL(
(L|i�uL���n��{Y�4�wOO{zy�$�	���'�ÖC�(�A#�4� ��s�����%�=���+G�ӥ�Oؕ�9�=2��G�!��4��eY��nWk�I�f�J�[���2��i�Aۉ����Y�J?X����Mj�	دG�k�_��~�*U��y�!���o۶���;�ӌ'��]��`��v�V��?ߑ�u8��".=q5�Up�iw�T̤�� �H�<2}��:���`�@G���&OHC^4P��񌎳"����b>_\.q<c8����F�x��r���δ#��Q��4��p��V��d�G     