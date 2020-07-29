### Notes
* Some large pre-trained vectors are not included. Download  from the [Sense2Vec official website](https://github.com/explosion/sense2vec) section below.
* The `s2v_reddit_2015_md` has been tested and working fine. The 2019 one is just too large and I didn't want to spend too much time to download them. 


### Pretrained vectors

To use the vectors, download the archive(s) and pass the extracted directory to
`Sense2Vec.from_disk` or `Sense2VecComponent.from_disk`. The vector files are
**attached to the GitHub release**. Large files have been split into multi-part
downloads.

| Vectors              |   Size | Description                  | 📥 Download (zipped)                                                                                                                                                                                                                                                                                                      |
| -------------------- | -----: | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `s2v_reddit_2019_lg` |   4 GB | Reddit comments 2019 (01-07) | [part 1](https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2019_lg.tar.gz.001), [part 2](https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2019_lg.tar.gz.002), [part 3](https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2019_lg.tar.gz.003) |
| `s2v_reddit_2015_md` | 573 MB | Reddit comments 2015         | [part 1](https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz)   


To merge the multi-part archives, you can run the following:

```bash
cat s2v_reddit_2019_lg.tar.gz.* > s2v_reddit_2019_lg.tar.gz
