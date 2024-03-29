  be sent instead.
        R   R7   i����R   (   RS   t   _Authenticatort   processR<   R�   R0   R:   (   RX   t	   mechanismt
   authobjectt   mechR[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   authenticateT  s    	c         C   s.   d } |  j  | � \ } } |  j | | | � S(   sT   (typ, [data]) = <instance>.capability()
        Fetch capabilities list from server.R   (   R�   R{   (   RX   R}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyRQ   q  s    c         C   s   |  j  d � S(   sR   Checkpoint mailbox on server.

        (typ, [data]) = <instance>.check()
        R   (   R�   (   RX   (    (    s   /usr/lib/python2.7/imaplib.pyt   checkz  s    c         C   s0   z |  j  d � \ } } Wd d |  _ X| | f S(   s�   Close currently selected mailbox.

        Deleted messages are removed from writable mailbox.
        This is the recommended command before 'LOGOUT'.

        (typ, [data]) = <instance>.close()
        R   NR   (   R�   R:   (   RX   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyRt   �  s    
c         C   s   |  j  d | | � S(   s�   Copy 'message_set' messages onto end of 'new_mailbox'.

        (typ, [data]) = <instance>.copy(message_set, new_mailbox)
        R   (   R�   (   RX   t   message_sett   new_mailbox(    (    s   /usr/lib/python2.7/imaplib.pyt   copy�  s    c         C   s   |  j  d | � S(   sP   Create new mailbox.

        (typ, [data]) = <instance>.create(mailbox)
        R   (   R�   (   RX   R�   (    (    s   /usr/lib/python2.7/imaplib.pyt   create�  s    c         C   s   |  j  d | � S(   sP   Delete old mailbox.

        (typ, [data]) = <instance>.delete(mailbox)
        R   (   R�   (   RX   R�   (    (    s   /usr/lib/python2.7/imaplib.pyt   delete�  s    c         C   s   |  j  d | | � S(   s�   Delete the ACLs (remove any rights) set for who on mailbox.

        (typ, [data]) = <instance>.deleteacl(mailbox, who)
        R   (   R�   (   RX   R�   t   who(    (    s   /usr/lib/python2.7/imaplib.pyt	   deleteacl�  s    c         C   s.   d } |  j  | � \ } } |  j | | | � S(   s�   Permanently remove deleted items from selected mailbox.

        Generates 'EXPUNGE' response for each deleted message.

        (typ, [data]) = <instance>.expunge()

        'data' is list of 'EXPUNGE'd message numbers in order received.
        R   (   R�   R{   (   RX   R}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   expunge�  s    	c         C   s4   d } |  j  | | | � \ } } |  j | | | � S(   s#  Fetch (parts of) messages.

        (typ, [data, ...]) = <instance>.fetch(message_set, message_parts)

        'message_parts' should be a string of selected parts
        enclosed in parentheses, eg: "(UID BODY[TEXT])".

        'data' are tuples of message part envelope and data.
        R   (   R�   R{   (   RX   R�   t   message_partsR}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   fetch�  s    
c         C   s+   |  j  d | � \ } } |  j | | d � S(   sX   Get the ACLs for a mailbox.

        (typ, [data]) = <instance>.getacl(mailbox)
        R   t   ACL(   R�   R{   (   RX   R�   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   getacl�  s    c         C   s1   |  j  d | | | � \ } } |  j | | d � S(   sa   (typ, [data]) = <instance>.getannotation(mailbox, entry, attribute)
        Retrieve ANNOTATIONs.R   t
   ANNOTATION(   R�   R{   (   RX   R�   t   entryt	   attributeR[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   getannotation�  s    c         C   s+   |  j  d | � \ } } |  j | | d � S(   s�   Get the quota root's resource usage and limits.

        Part of the IMAP4 QUOTA extension defined in rfc2087.

        (typ, [data]) = <instance>.getquota(root)
        R   t   QUOTA(   R�   R{   (   RX   t   rootR[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   getquota�  s    c         C   s^   |  j  d | � \ } } |  j | | d � \ } } |  j | | d � \ } } | | | g f S(   s�   Get the list of quota roots for the named mailbox.

        (typ, [[QUOTAROOT responses...], [QUOTA responses]]) = <instance>.getquotaroot(mailbox)
        R   R�   t	   QUOTAROOT(   R�   R{   (   RX   R�   R[   R\   t   quotat	   quotaroot(    (    s   /usr/lib/python2.7/imaplib.pyt   getquotaroot�  s    s   ""t   *c         C   s4   d } |  j  | | | � \ } } |  j | | | � S(   s�   List mailbox names in directory matching pattern.

        (typ, [data]) = <instance>.list(directory='""', pattern='*')

        'data' is list of LIST responses.
        R   (   R�   R{   (   RX   t	   directoryt   patternR}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   list�  s    c         C   sY   |  j  d | |  j | � � \ } } | d k rF |  j | d � � n  d |  _ | | f S(   s�   Identify client using plaintext password.

        (typ, [data]) = <instance>.login(user, password)

        NB: 'password' will be quoted.
        R   R7   i����R   (   R�   t   _quoteR0   R:   (   RX   t   usert   passwordR[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   login�  s
    $	c         C   s&   | | |  _  |  _ |  j d |  j � S(   sr    Force use of CRAM-MD5 authentication.

        (typ, [data]) = <instance>.login_cram_md5(user, password)
        s   CRAM-MD5(   R�   R�   R�   t   _CRAM_MD5_AUTH(   RX   R�   R�   (    (    s   /usr/lib/python2.7/imaplib.pyt   login_cram_md5  s    c         C   s0   d d l  } |  j d | j |  j | � j �  S(   s1    Authobject to use with CRAM-MD5 authentication. i����Nt    (   t   hmacR�   t   HMACR�   t	   hexdigest(   RX   t	   challengeR�   (    (    s   /usr/lib/python2.7/imaplib.pyR�     s    c         C   s~   d |  _  y |  j d � \ } } Wn% d d t j �  d  g } } n X|  j �  d |  j k rt d |  j d f S| | f S(   s|   Shutdown connection to server.

        (typ, [data]) = <instance>.logout()

        Returns server 'BYE' response.
        R   t   NOs   %s: %si   t   BYE(   R:   R�   t   syst   exc_infoRu   R>   (   RX   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   logout  s    	  "
c         C   s4   d } |  j  | | | � \ } } |  j | | | � S(   s�   List 'subscribed' mailbox names in directory matching pattern.

        (typ, [data, ...]) = <instance>.lsub(directory='""', pattern='*')

        'data' are tuples of message part envelope and data.
        R   (   R�   R{   (   RX   R�   R�   R}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   lsub,  s    c         C   s+   |  j  d | � \ } } |  j | | d � S(   s�   Show my ACLs for a mailbox (i.e. the rights that I have on mailbox).

        (typ, [data]) = <instance>.myrights(mailbox)
        R   (   R�   R{   (   RX   R�   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   myrights7  s    c         C   s.   d } |  j  | � \ } } |  j | | | � S(   sb    Returns IMAP namespaces ala rfc2342

        (typ, [data, ...]) = <instance>.namespace()
        R   (   R�   R{   (   RX   R}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt	   namespace?  s    c         C   s/   |  j  d k r" |  j |  j � n  |  j d � S(   sF   Send NOOP command.

        (typ, [data]) = <instance>.noop()
        i   R    (   R9   t   _dump_urR>   R�   (   RX   (    (    s   /usr/lib/python2.7/imaplib.pyR|   I  s    c         C   s:   d } |  j  | | | | | � \ } } |  j | | d � S(   s�   Fetch truncated part of a message.

        (typ, [data, ...]) = <instance>.partial(message_num, message_part, start, length)

        'data' is tuple of message part envelope and data.
        R!   R   (   R�   R{   (   RX   t   message_numt   message_partt   startt   lengthR}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   partialT  s    !c         C   s   d } |  j  d | � S(   s�   Assume authentication as "user".

        Allows an authorised administrator to proxy into any user's
        mailbox.

        (typ, [data]) = <instance>.proxyauth(user)
        R"   (   R�   (   RX   R�   R}   (    (    s   /usr/lib/python2.7/imaplib.pyt	   proxyauth`  s    	c         C   s   |  j  d | | � S(   sk   Rename old mailbox name to new.

        (typ, [data]) = <instance>.rename(oldmailbox, newmailbox)
        R#   (   R�   (   RX   t
   oldmailboxt
   newmailbox(    (    s   /usr/lib/python2.7/imaplib.pyt   renamem  s    c         G   sX   d } | r- |  j  | d | | � \ } } n |  j  | | � \ } } |  j | | | � S(   s�   Search mailbox for matching messages.

        (typ, [data]) = <instance>.search(charset, criterion, ...)

        'data' is space separated list of matching message numbers.
        R$   t   CHARSET(   R�   R{   (   RX   t   charsett   criteriaR}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   searchu  s
    !R�   c         C   s�   i  |  _  | |  _ | r! d } n d } |  j | | � \ } } | d k r^ d |  _ | | f Sd |  _ d |  j  k r� | r� |  j d k r� |  j |  j  � n  |  j d | � � n  | |  j  j d	 d
 g � f S(   st  Select a mailbox.

        Flush all untagged responses.

        (typ, [data]) = <instance>.select(mailbox='INBOX', readonly=False)

        'data' is count of messages in mailbox ('EXISTS' response).

        Mandated responses are ('FLAGS', 'EXISTS', 'RECENT', 'UIDVALIDITY'), so
        other responses should be obtained via <instance>.response('FLAGS') etc.
        R   R%   R7   R   R   s	   READ-ONLYi   s   %s is not writablet   EXISTSN(	   R>   RA   R�   R:   R9   R�   R4   t   getR;   (   RX   R�   R4   R}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   select�  s     				
	c         C   s   |  j  d | | | � S(   sZ   Set a mailbox acl.

        (typ, [data]) = <instance>.setacl(mailbox, who, what)
        R&   (   R�   (   RX   R�   R�   t   what(    (    s   /usr/lib/python2.7/imaplib.pyt   setacl�  s    c         G   s+   |  j  d | � \ } } |  j | | d � S(   s_   (typ, [data]) = <instance>.setannotation(mailbox[, entry, attribute]+)
        Set ANNOTATIONs.R'   R�   (   R�   R{   (   RX   t   argsR[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   setannotation�  s    c         C   s.   |  j  d | | � \ } } |  j | | d � S(   si   Set the quota root's resource limits.

        (typ, [data]) = <instance>.setquota(root, limits)
        R(   R�   (   R�   R{   (   RX   R�   t   limitsR[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   setquota�  s    c         G   s^   d } | d | d f d k r- d | } n  |  j  | | | | � \ } } |  j | | | � S(   s�   IMAP4rev1 extension SORT command.

        (typ, [data]) = <instance>.sort(sort_criteria, charset, search_criteria, ...)
        R)   i    i����R�   R�   s   (%s)(   R�   R�   (   R�   R{   (   RX   t   sort_criteriaR�   t   search_criteriaR}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   sort�  s
    c         C   s4   d } |  j  | | | � \ } } |  j | | | � S(   sp   Request named status conditions for mailbox.

        (typ, [data]) = <instance>.status(mailbox, names)
        R*   (   R�   R{   (   RX   R�   t   namesR}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   status�  s    c         C   sX   | d | d f d k r' d | } n  |  j  d | | | � \ } } |  j | | d � S(	   s�   Alters flag dispositions for messages in mailbox.

        (typ, [data]) = <instance>.store(message_set, command, flags)
        i    i����R�   R�   s   (%s)R+   R   (   R�   R�   (   R�   R{   (   RX   R�   t   commandR�   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   store�  s    c         C   s   |  j  d | � S(   sY   Subscribe to new mailbox.

        (typ, [data]) = <instance>.subscribe(mailbox)
        R,   (   R�   (   RX   R�   (    (    s   /usr/lib/python2.7/imaplib.pyt	   subscribe�  s    c         G   s7   d } |  j  | | | | � \ } } |  j | | | � S(   s�   IMAPrev1 extension THREAD command.

        (type, [data]) = <instance>.thread(threading_algorithm, charset, search_criteria, ...)
        R-   (   R�   R{   (   RX   t   threading_algorithmR�   R�   R}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   thread�  s    c         G   s�   | j  �  } | t k r. |  j d | � � n  |  j t | k rp |  j d | |  j d j t | � f � � n  d } |  j | | | � \ } } | d	 k r� | } n d } |  j | | | � S(
   s�   Execute "command arg ..." with messages identified by UID,
                rather than message number.

        (typ, [data]) = <instance>.uid(command, arg1, arg2, ...)

        Returns response appropriate to 'command'.
        s   Unknown IMAP4 UID command: %ss9   command %s illegal in state %s, only allowed in states %ss   , R.   R$   R)   R-   R   (   R$   R)   R-   (   RS   R_   R0   R:   t   joinR�   R{   (   RX   R�   R�   R}   R[   R\   (    (    s   /usr/lib/python2.7/imaplib.pyt   uid�  s    			c         C   s   |  j  d | � S(   s_   Unsubscribe from old mailbox.

        (typ, [data]) = <instance>.unsubscribe(mailbox)
        R/   (   R�   (   RX   R�   (    (    s   /usr/lib/python2.7/imaplib.pyt   unsubscribe  s    c         G   s;   | j  �  } | t k r+ |  j f t | <n  |  j | | � S(   s  Allow simple extension commands
                notified by server in CAPABILITY response.

        Assumes command is legal in current state.

        (typ, [data]) = <instance>.xatom(name, arg, ...)

        Returns response appropriate to extension command `name'.
        (   RS   R_   R:   R�   (   RX   R}   R�   (    (    s   /usr/lib/python2.7/imaplib.pyt   xatom  s    
c         C   s�   | d  k r d } n  |  j } |  j d k r\ |  j d | t | j | d � � | f � n  | | k r| | | j | � n | g | | <d  S(   NR5   i   s#   untagged_responses[%s] %s += ["%s"](   R;   R>   R9   RM   Ro   R�   R�   (   RX   R[   R\   t   ur(    (    s   /usr/lib/python2.7/imaplib.pyt   _append_untagged+  s     			&c         C   s2   |  j  j d � } | r. |  j | d � � n  d  S(   NR�   i����(   R>   R�   R3   (   RX   t   bye(    (    s   /usr/lib/python2.7/imaplib.pyt
   _check_bye9  s    c   
      G   s�  |  j  t | k rK d  |  _ |  j d | |  j  d j t | � f � � n  x* d D]" } | |  j k rR |  j | =qR qR Wd |  j k r� |  j r� |  j d � � n  |  j	 �  } d | | f } x9 | D]1 } | d  k r� q� n  d | |  j
 | � f } q� W|  j } | d  k	 r\d  |  _ t | � t |  j � k r=| } q\d  } d	 | t | � f } n  |  j d
 k r|  j d | � n |  j d | � y |  j d | t f � Wn/ t j t f k
 r�}	 |  j d |	 � � n X| d  k r�| Sx� x! |  j �  r|  j | r�| Sq�W| r,| |  j � } n  |  j d
 k rU|  j d t | � � n  y |  j | � |  j t � Wn/ t j t f k
 r�}	 |  j d |	 � � n X| s�Pq�q�W| S(   Ns9   command %s illegal in state %s, only allowed in states %ss   , R7   R�   t   BADs	   READ-ONLYs#   mailbox status changed to READ-ONLYs   %s %ss   %s {%s}i   s   > %ss   %s%ss   socket error