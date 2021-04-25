drop table if exists book cascade;

create table book (
    id numeric not null,
    author_id numeric,
    title text,
    primary key (id),
    constraint author_fk
        foreign key(author_id)
        references author(id)
);

create sequence book_seq
owned by book.id;
