import summershum.utils

import fedmsg
import logging
log = logging.getLogger("summershum")

def ingest(session, msg):
        log.info("Ingesting %r" % msg.get('filename'))
        fedmsg.publish(
            topic='ingest.start',
            msg=dict(original=msg),
        )
        try:
            summershum.utils.download_lookaside(msg)
            summershum.utils.get_sha1sum(session, msg)
        except Exception as e:
            log.error("Failed to ingest %r %r" % (msg.get('filename'), e))
            fedmsg.publish(
                topic='ingest.fail',
                msg=dict(
                    original=msg,
                    error=str(e),
                ),
            )
        else:
            log.info("Done ingesting %r" % msg.get('filename'))
            fedmsg.publish(
                topic='ingest.complete',
                msg=dict(original=msg),
            )
